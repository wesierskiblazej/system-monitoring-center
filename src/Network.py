#!/usr/bin/env python3

# Import modules
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os
import subprocess
import cairo

from locale import gettext as _tr

from Config import Config
from Performance import Performance


# Define class
class Network:

    # ----------------------- Always called when object is generated -----------------------
    def __init__(self):

        # Get GUI objects from file
        builder = Gtk.Builder()
        builder.add_from_file(os.path.dirname(os.path.realpath(__file__)) + "/../ui/NetworkTab.ui")

        # Get GUI objects
        self.grid1401 = builder.get_object('grid1401')
        self.drawingarea1401 = builder.get_object('drawingarea1401')
        self.button1401 = builder.get_object('button1401')
        self.label1401 = builder.get_object('label1401')
        self.label1402 = builder.get_object('label1402')
        self.label1403 = builder.get_object('label1403')
        self.label1404 = builder.get_object('label1404')
        self.label1405 = builder.get_object('label1405')
        self.label1406 = builder.get_object('label1406')
        self.label1407 = builder.get_object('label1407')
        self.label1408 = builder.get_object('label1408')
        self.label1409 = builder.get_object('label1409')
        self.label1410 = builder.get_object('label1410')
        self.label1411 = builder.get_object('label1411')
        self.label1412 = builder.get_object('label1412')
        self.label1413 = builder.get_object('label1413')

        # Connect GUI signals
        self.button1401.connect("clicked", self.on_button1401_clicked)
        self.drawingarea1401.connect("draw", self.on_drawingarea1401_draw)


    # ----------------------- "customizations menu" Button -----------------------
    def on_button1401_clicked(self, widget):

        from NetworkMenu import NetworkMenu
        NetworkMenu.popover1401p.set_relative_to(widget)
        NetworkMenu.popover1401p.set_position(1)
        NetworkMenu.popover1401p.popup()


    # ----------------------- Called for drawing Network download/upload speed as line chart -----------------------
    def on_drawingarea1401_draw(self, widget, ctx):

        # Get chart data history.
        chart_data_history = Config.chart_data_history
        chart_x_axis = list(range(0, chart_data_history))

        # Get performance data to be drawn.
        network_receive_speed = Performance.network_receive_speed[Performance.selected_network_card_number]
        network_send_speed = Performance.network_send_speed[Performance.selected_network_card_number]

        # Get chart colors.
        chart_line_color = Config.chart_line_color_network_speed_data
        chart_background_color = Config.chart_background_color_all_charts

        # Get drawingarea size. Therefore chart width and height is updated dynamically by using these values when window size is changed by user.
        chart_width = Gtk.Widget.get_allocated_width(widget)
        chart_height = Gtk.Widget.get_allocated_height(widget)

        # Draw and fill chart background.
        ctx.set_source_rgba(chart_background_color[0], chart_background_color[1], chart_background_color[2], chart_background_color[3])
        ctx.rectangle(0, 0, chart_width, chart_height)
        ctx.fill()

        # Draw horizontal and vertical gridlines.
        ctx.set_line_width(1)
        ctx.set_source_rgba(chart_line_color[0], chart_line_color[1], chart_line_color[2], 0.25 * chart_line_color[3])
        for i in range(3):
            ctx.move_to(0, chart_height/4*(i+1))
            ctx.rel_line_to(chart_width, 0)
        for i in range(4):
            ctx.move_to(chart_width/5*(i+1), 0)
            ctx.rel_line_to(0, chart_height)
        ctx.stroke()

        # Maximum performance data value is multiplied by 1.1 in order to scale chart when performance data is increased or decreased for preventing the line being out of the chart border.
        chart_y_limit = 1.1 * ((max(max(network_receive_speed), max(network_send_speed))) + 0.0000001)
        if Config.plot_network_download_speed == 1 and Config.plot_network_upload_speed == 0:
            chart_y_limit = 1.1 * (max(network_receive_speed) + 0.0000001)
        if Config.plot_network_download_speed == 0 and Config.plot_network_upload_speed == 1:
            chart_y_limit = 1.1 * (max(network_send_speed) + 0.0000001)

        # ---------- Start - This block of code is used in order to show maximum value of the chart as multiples of 1, 10, 100. ----------
        data_unit_for_chart_y_limit = 0
        if Config.performance_network_speed_data_unit >= 8:
            data_unit_for_chart_y_limit = 8
        try:
            chart_y_limit_str = f'{self.performance_data_unit_converter_func(chart_y_limit, data_unit_for_chart_y_limit, 0)}/s'
        # try-except is used in order to prevent errors if first initial function is not finished and "performance_data_unit_converter_func" is not run.
        except AttributeError:
            return
        chart_y_limit_split = chart_y_limit_str.split(" ")
        chart_y_limit_float = float(chart_y_limit_split[0])
        number_of_digits = len(str(int(chart_y_limit_split[0])))
        multiple = 10 ** (number_of_digits - 1)
        # "0.0001" is used in order to take decimal part of the numbers into account. For example, 1.9999 (2-0.0001). This number is enough because maximum precision of the performance data is "3" (1.234 MiB/s).
        number_to_get_next_multiple = chart_y_limit_float + (multiple - 0.0001)
        next_multiple = int(number_to_get_next_multiple - (number_to_get_next_multiple % multiple))
        self.label1413.set_text(f'{next_multiple} {chart_y_limit_split[1]}')
        # "0.0000001"'s are used in order to avoid errors if values are tried to be divided by "0".
        chart_y_limit = (chart_y_limit * next_multiple / (chart_y_limit_float + 0.0000001) + 0.0000001)
        # ---------- End - This block of code is used in order to show maximum value of the chart as multiples of 1, 10, 100. ----------

        # Draw outer border of the chart.
        ctx.set_source_rgba(chart_line_color[0], chart_line_color[1], chart_line_color[2], chart_line_color[3])
        ctx.rectangle(0, 0, chart_width, chart_height)
        ctx.stroke()

        if Config.plot_network_download_speed == 1:

            # Draw performance data.
            ctx.move_to(0, chart_height)
            ctx.rel_move_to(0, -chart_height*network_receive_speed[0]/chart_y_limit)
            for i in range(chart_data_history - 1):
                delta_x = (chart_width * chart_x_axis[i+1]/(chart_data_history-1)) - (chart_width * chart_x_axis[i]/(chart_data_history-1))
                delta_y = (chart_height*network_receive_speed[i+1]/chart_y_limit) - (chart_height*network_receive_speed[i]/chart_y_limit)
                ctx.rel_line_to(delta_x, -delta_y)

            # Change line color before drawing lines for closing the drawn line in order to revent drawing bolder lines due to overlapping.
            ctx.stroke_preserve()
            ctx.set_source_rgba(0, 0, 0, 0)

            # Close the drawn line to fill inside area of it.
            ctx.rel_line_to(0, chart_height*network_receive_speed[-1]/chart_y_limit)
            ctx.rel_line_to(-(chart_width), 0)
            ctx.close_path()

            # Fill the closed area.
            ctx.stroke_preserve()
            gradient_pattern = cairo.LinearGradient(0, 0, 0, chart_height)
            gradient_pattern.add_color_stop_rgba(0, chart_line_color[0], chart_line_color[1], chart_line_color[2], 0.55 * chart_line_color[3])
            gradient_pattern.add_color_stop_rgba(1, chart_line_color[0], chart_line_color[1], chart_line_color[2], 0.10 * chart_line_color[3])
            ctx.set_source(gradient_pattern)
            ctx.fill()

        if Config.plot_network_upload_speed == 1:

            ctx.set_source_rgba(chart_line_color[0], chart_line_color[1], chart_line_color[2], chart_line_color[3])
            ctx.set_dash([5, 3])

            # Draw performance data.
            ctx.move_to(0, chart_height)
            ctx.rel_move_to(0, -chart_height*network_send_speed[0]/chart_y_limit)
            for i in range(chart_data_history - 1):
                delta_x = (chart_width * chart_x_axis[i+1]/(chart_data_history-1)) - (chart_width * chart_x_axis[i]/(chart_data_history-1))
                delta_y = (chart_height*network_send_speed[i+1]/chart_y_limit) - (chart_height*network_send_speed[i]/chart_y_limit)
                ctx.rel_line_to(delta_x, -delta_y)

            # Change line color before drawing lines for closing the drawn line in order to revent drawing bolder lines due to overlapping.
            ctx.stroke_preserve()
            ctx.set_source_rgba(0, 0, 0, 0)

            # Close the drawn line to fill inside area of it.
            ctx.rel_line_to(0, chart_height*network_send_speed[-1]/chart_y_limit)
            ctx.rel_line_to(-(chart_width), 0)
            ctx.close_path()


    # ----------------------------------- Network - Initial Function -----------------------------------
    def network_initial_func(self):

        # Define data unit conversion function objects in for lower CPU usage.
        self.performance_define_data_unit_converter_variables_func = Performance.performance_define_data_unit_converter_variables_func
        self.performance_data_unit_converter_func = Performance.performance_data_unit_converter_func

        # Define data unit conversion variables before they are used.
        self.performance_define_data_unit_converter_variables_func()

        network_card_list = Performance.network_card_list
        selected_network_card_number = Performance.selected_network_card_number
        selected_network_card = network_card_list[selected_network_card_number]

        # Get device vendor and model names
        device_vendor_name = "-"
        device_model_name = "-"
        # Get device vendor and model names if it is not a virtual device.
        if os.path.isdir("/sys/devices/virtual/net/" + selected_network_card) == False:
            # Check if there is a "modalias" file. Some network interfaces (such as usb0, usb1, etc.) may not have this file.
            if os.path.isfile("/sys/class/net/" + selected_network_card + "/device/modalias") == True:
                # Read device vendor and model ids by reading "modalias" file.
                with open("/sys/class/net/" + selected_network_card + "/device/modalias") as reader:
                    modalias_output = reader.read().strip()
                device_vendor_name, device_model_name, _, _ = Performance.performance_get_device_vendor_model_func(modalias_output)
                if device_vendor_name == "Unknown":
                    device_vendor_name = "[" + _tr("Unknown") + "]"
                if device_model_name == "Unknown":
                    device_model_name = "[" + _tr("Unknown") + "]"
            network_card_device_model_name = f'{device_vendor_name} - {device_model_name}'
        # Get device vendor and model names if it is a virtual device.
        else:
            # lo (Loopback Device) is a system device and it is not a physical device. It could not be found in "pci.ids" file.
            if selected_network_card == "lo":
                network_card_device_model_name = "Loopback Device"
            else:
                network_card_device_model_name = "[" + _tr("Virtual Network Interface") + "]"

        # Get connection_type
        if selected_network_card.startswith("en"):
            connection_type = _tr("Ethernet")
        elif selected_network_card.startswith("wl"):
            connection_type = _tr("Wi-Fi")
        else:
            connection_type = "-"

        # Get network_card_mac_address
        try:
            with open("/sys/class/net/" + selected_network_card + "/address") as reader:
                network_card_mac_address = reader.read().strip().upper()
        # Some network interfaces (such as some of the virtual network interfaces) may not have a MAC address.
        except FileNotFoundError:
            network_card_mac_address = "-"

        # Get network_address_ipv4, network_address_ipv6
        ip_output_lines = (subprocess.check_output(["ip", "a", "show", selected_network_card], shell=False)).decode().strip().split("\n")
        network_address_ipv4 = "-"
        network_address_ipv6 = "-"
        for line in ip_output_lines:
            if "inet " in line:
                network_address_ipv4 = line.split()[1].split("/")[0]
            if "inet6 " in line:
                network_address_ipv6 = line.split()[1].split("/")[0]


        # Set Network tab label texts by using information get
        self.label1401.set_text(network_card_device_model_name)
        self.label1402.set_text(selected_network_card)
        self.label1407.set_text(connection_type)
        self.label1410.set_text(network_address_ipv4)
        self.label1411.set_text(network_address_ipv6)
        self.label1412.set_text(network_card_mac_address)

        self.initial_already_run = 1


    # ----------------------------------- Network - Initial Function -----------------------------------
    def network_loop_func(self):

        network_card_list = Performance.network_card_list
        selected_network_card_number = Performance.selected_network_card_number
        selected_network_card = network_card_list[selected_network_card_number]

        # Run "network_initial_func" if selected network card is changed since the last loop.
        try:
            if self.selected_network_card_prev != selected_network_card:
                self.network_initial_func()
        # Avoid errors if this is first loop of the function.
        except AttributeError:
            pass
        self.selected_network_card_prev = selected_network_card

        network_receive_speed = Performance.network_receive_speed
        network_send_speed = Performance.network_send_speed
        network_receive_bytes = Performance.network_receive_bytes
        network_send_bytes = Performance.network_send_bytes

        performance_network_speed_data_precision = Config.performance_network_speed_data_precision
        performance_network_data_data_precision = Config.performance_network_data_data_precision
        performance_network_speed_data_unit = Config.performance_network_speed_data_unit
        performance_network_data_data_unit = Config.performance_network_data_data_unit

        self.drawingarea1401.queue_draw()

        # Get network_card_connected
        # Get the information of if network card is connected by usng "/sys/class/net/" file.
        with open("/sys/class/net/" + selected_network_card + "/operstate") as reader:
            network_info = reader.read().strip()
        if network_info == "up":
            network_card_connected = _tr("Yes")
        elif network_info == "down":
            network_card_connected = _tr("No")
        elif network_info == "unknown":
            network_card_connected = f'[{_tr("Unknown")}]'
        else:
            network_card_connected = network_info

        # Get network_ssid
        try:                                                                                      
            nmcli_output_lines = (subprocess.check_output(["nmcli", "-get-values", "DEVICE,CONNECTION", "device", "status"], shell=False)).decode().strip().split("\n")
        # Avoid errors because Network Manager (which is required for running "nmcli" command) may not be installed on all systems (very rare).
        except FileNotFoundError:
            network_ssid = f'[{_tr("Unknown")}]'
        # Check if "nmcli_output_lines" value is get.
        if "nmcli_output_lines" in locals():
            for line in nmcli_output_lines:
                line_splitted = line.split(":")
                if selected_network_card == line_splitted[0]:
                    network_ssid = line_splitted[1].strip()
                    break
        # "network_ssid" value is get as "" if selected network card is not connected a Wi-Fi network.
        if network_ssid == "":
            network_ssid = "-"

        # Get network_signal_strength
        network_signal_strength = "-"
        # Translated value have to be used by using gettext constant. Not "Yes".
        if "wl" in selected_network_card and network_card_connected == _tr("Yes"):
            with open("/proc/net/wireless") as reader:
                proc_net_wireless_output_lines = reader.read().strip().split("\n")
            for line in proc_net_wireless_output_lines:
                line_splitted = line.split()
                if selected_network_card == line_splitted[0].split(":")[0]:
                    # "split(".")" is used in order to remove "." at the end of the signal value.
                    network_signal_strength = line_splitted[2].split(".")[0]
                    break


        # Set and update Network tab label texts by using information get
        self.label1403.set_text(f'{self.performance_data_unit_converter_func(network_receive_speed[selected_network_card_number][-1], performance_network_speed_data_unit, performance_network_speed_data_precision)}/s')
        self.label1404.set_text(f'{self.performance_data_unit_converter_func(network_send_speed[selected_network_card_number][-1], performance_network_speed_data_unit, performance_network_speed_data_precision)}/s')
        self.label1405.set_text(self.performance_data_unit_converter_func(network_receive_bytes[selected_network_card_number], performance_network_data_data_unit, performance_network_data_data_precision))
        self.label1406.set_text(self.performance_data_unit_converter_func(network_send_bytes[selected_network_card_number], performance_network_data_data_unit, performance_network_data_data_precision))
        self.label1408.set_text(f'{network_card_connected} - {network_ssid}')
        self.label1409.set_text(network_signal_strength)


# Generate object
Network = Network()


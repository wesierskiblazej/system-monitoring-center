#!/usr/bin/env python3

# Import modules
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os

from locale import gettext as _tr

from Config import Config
from MainGUI import MainGUI
from Performance import Performance


# Define class
class SettingsGUI:

    # ----------------------- Always called when object is generated -----------------------
    def __init__(self):

        # Get GUI objects from file
        builder2001 = Gtk.Builder()
        builder2001.add_from_file(os.path.dirname(os.path.realpath(__file__)) + "/../ui/SettingsWindow.ui")

        # Get GUI objects
        self.window2001 = builder2001.get_object('window2001')
        self.button2002 = builder2001.get_object('button2002')
        self.button2003 = builder2001.get_object('button2003')
        self.button2004 = builder2001.get_object('button2004')
        self.combobox2001 = builder2001.get_object('combobox2001')
        self.combobox2002 = builder2001.get_object('combobox2002')
        self.combobox2003 = builder2001.get_object('combobox2003')
        self.combobox2004 = builder2001.get_object('combobox2004')
        self.checkbutton2001 = builder2001.get_object('checkbutton2001')
        self.checkbutton2002 = builder2001.get_object('checkbutton2002')
        self.checkbutton2003 = builder2001.get_object('checkbutton2003')
        self.checkbutton2004 = builder2001.get_object('checkbutton2004')
        self.checkbutton2005 = builder2001.get_object('checkbutton2005')
        self.checkbutton2006 = builder2001.get_object('checkbutton2006')
        self.checkbutton2007 = builder2001.get_object('checkbutton2007')
        self.checkbutton2008 = builder2001.get_object('checkbutton2008')
        self.checkbutton2009 = builder2001.get_object('checkbutton2009')
        self.checkbutton2010 = builder2001.get_object('checkbutton2010')
        self.checkbutton2011 = builder2001.get_object('checkbutton2011')
        self.checkbutton2012 = builder2001.get_object('checkbutton2012')
        self.spinbutton2001 = builder2001.get_object('spinbutton2001')

        # Connect GUI signals
        self.window2001.connect("delete-event", self.on_window2001_delete_event)
        self.window2001.connect("show", self.on_window2001_show)
        self.button2002.connect("clicked", self.on_button2002_clicked)
        self.button2003.connect("clicked", self.on_button2003_clicked)
        self.button2004.connect("clicked", self.on_button2004_clicked)

        # Define data lists in order to add them into comboboxes.
        self.update_interval_list = [0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 3.0, 5.0, 10.0]
        self.chart_data_history_list = [30, 60, 90, 120, 150, 180, 300, 600, 1200]
        self.default_main_tab_list = [_tr("Performance"), _tr("Processes"), _tr("Users"), _tr("Startup"), _tr("Services"), _tr("System")]
        self.performance_tab_default_sub_tab_list = [_tr("CPU"), _tr("RAM"), _tr("Disk"), _tr("Network"), _tr("GPU"), _tr("Sensors")]


    # ----------------------- Called for connecting some of the signals in order to disconnect them for setting GUI -----------------------
    def settings_connect_signals_func(self):

        self.combobox2001.connect("changed", self.on_combobox2001_changed)
        self.combobox2002.connect("changed", self.on_combobox2002_changed)
        self.combobox2003.connect("changed", self.on_combobox2003_changed)
        self.combobox2004.connect("changed", self.on_combobox2004_changed)
        self.checkbutton2001.connect("toggled", self.on_checkbutton2001_toggled)
        self.checkbutton2002.connect("toggled", self.on_checkbutton2002_toggled)
        self.checkbutton2003.connect("toggled", self.on_checkbutton2003_toggled)
        self.checkbutton2004.connect("toggled", self.on_add_remove_checkbuttons_toggled)
        self.checkbutton2005.connect("toggled", self.on_add_remove_checkbuttons_toggled)
        self.checkbutton2006.connect("toggled", self.on_add_remove_checkbuttons_toggled)
        self.checkbutton2007.connect("toggled", self.on_add_remove_checkbuttons_toggled)
        self.checkbutton2008.connect("toggled", self.on_add_remove_checkbuttons_toggled)
        self.checkbutton2009.connect("toggled", self.on_add_remove_checkbuttons_toggled)
        self.checkbutton2010.connect("toggled", self.on_add_remove_checkbuttons_toggled)
        self.checkbutton2011.connect("toggled", self.on_add_remove_checkbuttons_toggled)
        self.checkbutton2012.connect("toggled", self.on_checkbutton2012_toggled)
        self.spinbutton2001.connect("value-changed", self.on_spinbutton2001_value_changed)


    # ----------------------- Called for disconnecting some of the signals in order to connect them for setting GUI -----------------------
    def settings_disconnect_signals_func(self):

        self.combobox2001.disconnect_by_func(self.on_combobox2001_changed)
        self.combobox2002.disconnect_by_func(self.on_combobox2002_changed)
        self.combobox2003.disconnect_by_func(self.on_combobox2003_changed)
        self.combobox2004.disconnect_by_func(self.on_combobox2004_changed)
        self.checkbutton2001.disconnect_by_func(self.on_checkbutton2001_toggled)
        self.checkbutton2002.disconnect_by_func(self.on_checkbutton2002_toggled)
        self.checkbutton2003.disconnect_by_func(self.on_checkbutton2003_toggled)
        self.checkbutton2004.disconnect_by_func(self.on_add_remove_checkbuttons_toggled)
        self.checkbutton2005.disconnect_by_func(self.on_add_remove_checkbuttons_toggled)
        self.checkbutton2006.disconnect_by_func(self.on_add_remove_checkbuttons_toggled)
        self.checkbutton2007.disconnect_by_func(self.on_add_remove_checkbuttons_toggled)
        self.checkbutton2008.disconnect_by_func(self.on_add_remove_checkbuttons_toggled)
        self.checkbutton2009.disconnect_by_func(self.on_add_remove_checkbuttons_toggled)
        self.checkbutton2010.disconnect_by_func(self.on_add_remove_checkbuttons_toggled)
        self.checkbutton2011.disconnect_by_func(self.on_add_remove_checkbuttons_toggled)
        self.checkbutton2012.disconnect_by_func(self.on_checkbutton2012_toggled)
        self.spinbutton2001.disconnect_by_func(self.on_spinbutton2001_value_changed)


    # ----------------------- Called for running code/functions when GUI is shown -----------------------
    def on_window2001_show(self, widget):

        try:
            self.settings_disconnect_signals_func()
        except TypeError:
            pass
        self.settings_gui_general_settings_tab_set_func()
        self.settings_gui_floating_summary_settings_tab_set_func()
        self.settings_connect_signals_func()


    # ----------------------- Called for running code/functions when window is closed -----------------------
    def on_window2001_delete_event(self, widget, event):

        self.window2001.hide()
        return True


    # ----------------------- "Update interval" Combobox -----------------------
    def on_combobox2001_changed(self, widget):

        Config.update_interval = self.update_interval_list[widget.get_active()]

        Config.config_save_func()

        # Apply changes immediately (without waiting update interval).
        self.settings_gui_apply_settings_immediately_func()


    # ----------------------- "Chart data history" Combobox -----------------------
    def on_combobox2002_changed(self, widget):

        Config.chart_data_history = self.chart_data_history_list[widget.get_active()]

        Config.config_save_func()

        # Apply changes immediately (without waiting update interval).
        self.settings_gui_set_chart_data_history_func()
        self.settings_gui_apply_settings_immediately_func()


    # ----------------------- "Show performance summary on the headerbar" Checkbutton -----------------------
    def on_checkbutton2001_toggled(self, widget):

        from PerformanceSummaryHeaderbar import PerformanceSummaryHeaderbar

        # Add performance summary to the main window headerbar if preferred.
        if widget.get_active() == True:
            Config.performance_summary_on_the_headerbar = 1
            MainGUI.headerbar1.pack_start(PerformanceSummaryHeaderbar.grid101)

        # Remove performance summary from the main window headerbar if preferred.
        if widget.get_active() == False:
            Config.performance_summary_on_the_headerbar = 0
            MainGUI.headerbar1.remove(PerformanceSummaryHeaderbar.grid101)

        Config.config_save_func()


    # ----------------------- "Remember last opened tabs" Checkbutton -----------------------
    def on_checkbutton2002_toggled(self, widget):

        # Get currently opened tabs and save them if preferred.
        if widget.get_active() == True:
            Config.remember_last_opened_tabs_on_application_start = 1
            self.combobox2003.set_sensitive(False)
            self.combobox2004.set_sensitive(False)
            self.settings_gui_default_tab_func()

        # Set setting for not remembering las opened tabs if preferred.
        if widget.get_active() == False:
            Config.remember_last_opened_tabs_on_application_start = 0
            self.combobox2003.set_sensitive(True)
            self.combobox2004.set_sensitive(True)

        Config.config_save_func()


    # ----------------------- "Default main tab" Combobox -----------------------
    def on_combobox2003_changed(self, widget):

        # Get selected tab as default main tab and save it if preferred.
        Config.default_main_tab = widget.get_active()
        Config.config_save_func()


    # ----------------------- "Performance tab default sub-tab" Combobox -----------------------
    def on_combobox2004_changed(self, widget):

        # Get selected tab as Performance tab default sub-tab and save it if preferred.
        Config.performance_tab_default_sub_tab = widget.get_active()
        Config.config_save_func()


    # ----------------------- "Remember last selected hardware" Checkbutton -----------------------
    def on_checkbutton2003_toggled(self, widget):

        if widget.get_active() == True:
            Config.remember_last_selected_hardware = 1

        if widget.get_active() == False:
            Config.remember_last_selected_hardware = 0

        Config.config_save_func()


    # ----------------------- "Remember window size" Checkbutton -----------------------
    def on_checkbutton2012_toggled(self, widget):

        # Get window state (if full screen or not), window size (width, height) and save if preferred.
        if widget.get_active() == True:
            remember_window_size_value = 1
            main_window_state = MainGUI.window1.is_maximized()
            if main_window_state == True:
                main_window_state = 1
            if main_window_state == False:
                main_window_state = 0
            main_window_width, main_window_height = MainGUI.window1.get_size()
            Config.remember_window_size = [remember_window_size_value, main_window_state, main_window_width, main_window_height]

        # Reset window size/state settings if preferred.
        if widget.get_active() == False:
            remember_window_size_value = 0
            main_window_state = 0
            main_window_width, main_window_height = MainGUI.window1.get_default_size()
            Config.remember_window_size = [remember_window_size_value, main_window_state, main_window_width, main_window_height]

        Config.config_save_func()


    # ----------------------- "Reset general settings to defaults" Button -----------------------
    def on_button2002_clicked(self, widget):

        Config.config_default_general_general_func()
        Config.config_save_func()
        # Set "General" tab of the Settings window without disconnecting signals of the widgets in order to use these signals to reset the settings.
        self.settings_gui_general_settings_tab_set_func()

        # Length of performance data lists (cpu_usage_percent_ave, ram_usage_percent_ave, ...) have to be set after "chart_data_history" setting is reset in order to avoid errors.
        self.settings_gui_set_chart_data_history_func()

        # Apply selected CPU core, disk, network card changes
        Performance.performance_set_selected_cpu_core_func()
        Performance.performance_set_selected_disk_func()
        Performance.performance_set_selected_network_card_func()
        # Apply selected GPU changes
        try:
            from MainGUI import Gpu
            Gpu.gpu_get_gpu_list_and_set_selected_gpu_func()
        # "try-except" is used in order to avoid errors because "gpu_get_gpu_list_and_set_selected_gpu_func" module requires some modules in the Gpu module they are imported if Gpu tab is switched on.
        except ImportError:
            pass

        # Apply changes immediately (without waiting update interval).
        self.settings_gui_apply_settings_immediately_func()


    # ----------------------- "Floating Summary - Window transparency" Spinbutton -----------------------
    def on_spinbutton2001_value_changed(self, widget):

        Config.floating_summary_window_transparency = widget.get_value()
        Config.config_save_func()


    # ----------------------- "Floating Summary - Show/Hide Performance Information - CPU Usage Average, RAM Usage, etc." Checkbuttons -----------------------
    def on_add_remove_checkbuttons_toggled(self, widget):

        self.settings_gui_add_remove_floating_summary_performance_information_func()


    # ----------------------- "Reset floating summary window settings to defaults" Button -----------------------
    def on_button2003_clicked(self, widget):

        # Get current "show_floating_summary" setting, reset all Floating Summary settings and set "show_floating_summary" by using the get setting in order to reset only other settings of the Floating Summary.
        show_floating_summary_current_setting = Config.show_floating_summary
        Config.config_default_general_floating_summary_func()
        Config.show_floating_summary = show_floating_summary_current_setting
        Config.config_save_func()
        self.settings_disconnect_signals_func()
        self.settings_gui_floating_summary_settings_tab_set_func()
        self.settings_connect_signals_func()


    # ----------------------- "Reset all settings of the application to defaults" Button -----------------------
    def on_button2004_clicked(self, widget):

        self.settings_gui_reset_all_settings_warning_dialog()

        if self.warning_dialog2001_response == Gtk.ResponseType.YES:

            Config.config_default_reset_all_func()
            Config.config_save_func()
            self.settings_gui_general_settings_tab_set_func()
            self.settings_disconnect_signals_func()
            self.settings_gui_floating_summary_settings_tab_set_func()
            self.settings_connect_signals_func()

            # Length of performance data lists (cpu_usage_percent_ave, ram_usage_percent_ave, ...) have to be set after "chart_data_history" setting is reset in order to avoid errors.
            self.settings_gui_set_chart_data_history_func()

            # Apply selected CPU core, disk, network card changes
            Performance.performance_set_selected_cpu_core_func()
            Performance.performance_set_selected_disk_func()
            Performance.performance_set_selected_network_card_func()
            # Apply selected GPU changes
            try:
                from MainGUI import Gpu
                Gpu.gpu_get_gpu_list_and_set_selected_gpu_func()
            # "try-except" is used in order to avoid errors because "gpu_get_gpu_list_and_set_selected_gpu_func" module requires some modules in the Gpu module they are imported if Gpu tab is switched on.
            except ImportError:
                pass

            # Apply changes immediately (without waiting update interval).
            self.settings_gui_apply_settings_immediately_func()

            # "try-catch" is used in order to avoid errors because "Processes" may not be loaded.
            try:
                from MainGUI import Processes
                Processes.processes_expand_and_filter_radiobutton_preferences_func()
            except ImportError:
                pass


    # ----------------------- Called for setting "General" tab GUI items -----------------------
    def settings_gui_general_settings_tab_set_func(self):

        # Set GUI preferences for "update interval" setting
        liststore2001 = Gtk.ListStore()
        liststore2001.set_column_types([str])
        self.combobox2001.set_model(liststore2001)
        # Clear combobox in order to prevent adding the same items when the function is called again.
        self.combobox2001.clear()
        renderer_text = Gtk.CellRendererText()
        self.combobox2001.pack_start(renderer_text, True)
        self.combobox2001.add_attribute(renderer_text, "text", 0)
        for value in self.update_interval_list:
            liststore2001.append([str(value)])
        self.combobox2001.set_active(self.update_interval_list.index(Config.update_interval))

        # Set GUI preferences for "chart data history" setting
        liststore2002 = Gtk.ListStore()
        liststore2002.set_column_types([str])
        self.combobox2002.set_model(liststore2002)
        # Clear combobox in order to prevent adding the same items when the function is called again.
        self.combobox2002.clear()
        renderer_text = Gtk.CellRendererText()
        self.combobox2002.pack_start(renderer_text, True)
        self.combobox2002.add_attribute(renderer_text, "text", 0)
        for value in self.chart_data_history_list:
            liststore2002.append([str(value)])
        self.combobox2002.set_active(self.chart_data_history_list.index(Config.chart_data_history))

        # Set GUI preferences for "show performance summary on the headerbar" setting
        if Config.performance_summary_on_the_headerbar == 1:
            self.checkbutton2001.set_active(True)
        if Config.performance_summary_on_the_headerbar == 0:
            self.checkbutton2001.set_active(False)

        # Set GUI preferences for "remember last opened tabs" setting
        if Config.remember_last_opened_tabs_on_application_start == 1:
            self.checkbutton2002.set_active(True)
        if Config.remember_last_opened_tabs_on_application_start == 0:
            self.checkbutton2002.set_active(False)

        # Set GUI preferences for "defult main tab" setting
        liststore2003 = Gtk.ListStore()
        liststore2003.set_column_types([str])
        self.combobox2003.set_model(liststore2003)
        # Clear combobox in order to prevent adding the same items when the function is called again.
        self.combobox2003.clear()
        renderer_text = Gtk.CellRendererText()
        self.combobox2003.pack_start(renderer_text, True)
        self.combobox2003.add_attribute(renderer_text, "text", 0)
        for value in self.default_main_tab_list:
            liststore2003.append([value])
        self.combobox2003.set_active(Config.default_main_tab)
        if Config.remember_last_opened_tabs_on_application_start == 1:
            self.combobox2003.set_sensitive(False)
        if Config.remember_last_opened_tabs_on_application_start == 0:
            self.combobox2003.set_sensitive(True)

        # Set GUI preferences for "performance tab default sub-tab" setting
        liststore2004 = Gtk.ListStore()
        liststore2004.set_column_types([str])
        self.combobox2004.set_model(liststore2004)
        # Clear combobox in order to prevent adding the same items when the function is called again.
        self.combobox2004.clear()
        renderer_text = Gtk.CellRendererText()
        self.combobox2004.pack_start(renderer_text, True)
        self.combobox2004.add_attribute(renderer_text, "text", 0)
        for value in self.performance_tab_default_sub_tab_list:
            liststore2004.append([value])
        self.combobox2004.set_active(Config.performance_tab_default_sub_tab)
        if Config.remember_last_opened_tabs_on_application_start == 1:
            self.combobox2004.set_sensitive(False)
        if Config.remember_last_opened_tabs_on_application_start == 0:
            self.combobox2004.set_sensitive(True)

        # Set GUI preferences for "remember last selected hardware" setting
        if Config.remember_last_selected_hardware == 1:
            self.checkbutton2003.set_active(True)
        if Config.remember_last_selected_hardware == 0:
            self.checkbutton2003.set_active(False)

        # Set GUI preferences for "remember window size" setting
        if Config.remember_window_size[0] == 1:
            self.checkbutton2012.set_active(True)
        if Config.remember_window_size[0] == 0:
            self.checkbutton2012.set_active(False)


    # ----------------------- Called for setting "Floating Summary" tab GUI items -----------------------
    def settings_gui_floating_summary_settings_tab_set_func(self):

        # Set GUI preferences for "window transparency" setting
        adjustment2001 = Gtk.Adjustment().new(Config.floating_summary_window_transparency, 0.0, 1.0, 0.05, 0.1, 0.0)
        self.spinbutton2001.set_digits(2)
        self.spinbutton2001.set_adjustment(adjustment2001)
        adjustment2001.set_value(Config.floating_summary_window_transparency)

        # Set GUI preferences for "show/hide information" setting
        if 0 in Config.floating_summary_data_shown:
            self.checkbutton2004.set_active(True)
        else:
            self.checkbutton2004.set_active(False)
        if 1 in Config.floating_summary_data_shown:
            self.checkbutton2005.set_active(True)
        else:
            self.checkbutton2005.set_active(False)
        if 2 in Config.floating_summary_data_shown:
            self.checkbutton2006.set_active(True)
        else:
            self.checkbutton2006.set_active(False)
        if 3 in Config.floating_summary_data_shown:
            self.checkbutton2007.set_active(True)
        else:
            self.checkbutton2007.set_active(False)
        if 4 in Config.floating_summary_data_shown:
            self.checkbutton2008.set_active(True)
        else:
            self.checkbutton2008.set_active(False)
        if 5 in Config.floating_summary_data_shown:
            self.checkbutton2009.set_active(True)
        else:
            self.checkbutton2009.set_active(False)
        if 6 in Config.floating_summary_data_shown:
            self.checkbutton2010.set_active(True)
        else:
            self.checkbutton2010.set_active(False)
        if 7 in Config.floating_summary_data_shown:
            self.checkbutton2011.set_active(True)
        else:
            self.checkbutton2011.set_active(False)


    # ----------------------- Called for adding/removing Floating Summary performance information -----------------------
    def settings_gui_add_remove_floating_summary_performance_information_func(self):

        Config.floating_summary_data_shown = []

        if self.checkbutton2004.get_active() == True:
            Config.floating_summary_data_shown.append(0)
        if self.checkbutton2005.get_active() == True:
            Config.floating_summary_data_shown.append(1)
        if self.checkbutton2006.get_active() == True:
            Config.floating_summary_data_shown.append(2)
        if self.checkbutton2007.get_active() == True:
            Config.floating_summary_data_shown.append(3)
        if self.checkbutton2008.get_active() == True:
            Config.floating_summary_data_shown.append(4)
        if self.checkbutton2009.get_active() == True:
            Config.floating_summary_data_shown.append(5)
        if self.checkbutton2010.get_active() == True:
            Config.floating_summary_data_shown.append(6)
        if self.checkbutton2011.get_active() == True:
            Config.floating_summary_data_shown.append(7)

        Config.config_save_func()


    # ----------------------- Called for trimming/adding performance data lists (cpu_usage_percent_ave, ram_usage_percent, ...) for chart data history when "chart_data_history" preference is changed -----------------------
    def settings_gui_set_chart_data_history_func(self):

        chart_data_history_current = len(Performance.cpu_usage_percent_ave)                       # Get current chart_data_history length. This value is same for all performance data lists (cpu_usage_percent_ave, ram_usage_percent, ...).
        chart_data_history_new = Config.chart_data_history
        if chart_data_history_current > chart_data_history_new:                                   # Trim beginning part of the lists if new "chart_data_history" value is smaller than the old value.
            Performance.cpu_usage_percent_ave = Performance.cpu_usage_percent_ave[chart_data_history_current-chart_data_history_new:]    # "cpu_usage_percent_ave" list has no sub-lists and trimming is performed in this way.
            cpu_usage_percent_per_core_len = len(Performance.cpu_usage_percent_per_core)
            for i in range(cpu_usage_percent_per_core_len):
                Performance.cpu_usage_percent_per_core[i] = Performance.cpu_usage_percent_per_core[i][chart_data_history_current-chart_data_history_new:]    # "cpu_usage_percent_per_core" list has sub-lists and trimming is performed for every sub-lists (for every CPU core).
            Performance.ram_usage_percent = Performance.ram_usage_percent[chart_data_history_current-chart_data_history_new:]    # "ram_usage_percent" list has no sub-lists and trimming is performed in this way.
            disk_read_speed_len = len(Performance.disk_read_speed)
            for i in range(disk_read_speed_len):
                Performance.disk_read_speed[i] = Performance.disk_read_speed[i][chart_data_history_current-chart_data_history_new:]    # "disk_read_speed" list has sub-lists and trimming is performed for every sub-lists (for every disk).
                Performance.disk_write_speed[i] = Performance.disk_write_speed[i][chart_data_history_current-chart_data_history_new:]    # "disk_write_speed" list has sub-lists and trimming is performed for every sub-lists (for every disk).
            network_receive_speed_len = len(Performance.network_receive_speed)
            for i in range(network_receive_speed_len):
                Performance.network_receive_speed[i] = Performance.network_receive_speed[i][chart_data_history_current-chart_data_history_new:]    # "network_receive_speed" list has sub-lists and trimming is performed for every sub-lists (for every network card).
                Performance.network_send_speed[i] = Performance.network_send_speed[i][chart_data_history_current-chart_data_history_new:]    # "network_send_speed" list has sub-lists and trimming is performed for every sub-lists (for every network card).
            if MainGUI.radiobutton1005.get_active() == True:
                from Gpu import Gpu
                Gpu.fps_count = Gpu.fps_count[chart_data_history_current-chart_data_history_new:]     # "fps_count" list has no sub-lists and trimming is performed in this way.
        if chart_data_history_current < chart_data_history_new:                                   # Add list of zeroes to the beginning part of the lists if new "chart_data_history" value is bigger than the old value.
            list_to_add = [0] * (chart_data_history_new - chart_data_history_current)             # Generate list of zeroes for adding to the beginning of te lists.
            Performance.cpu_usage_percent_ave = list_to_add + Performance.cpu_usage_percent_ave   # "cpu_usage_percent_ave" list has no sub-lists and addition is performed in this way.
            cpu_usage_percent_per_core_len = len(Performance.cpu_usage_percent_per_core)
            for i in range(cpu_usage_percent_per_core_len):
                Performance.cpu_usage_percent_per_core[i] = list_to_add + Performance.cpu_usage_percent_per_core[i]     # "cpu_usage_percent_per_core" list has sub-lists and addition is performed for every sub-lists (for every CPU core).
            Performance.ram_usage_percent = list_to_add + Performance.ram_usage_percent           # "ram_usage_percent" list has no sub-lists and addition is performed in this way.
            disk_read_speed_len = len(Performance.disk_read_speed)
            for i in range(disk_read_speed_len):
                Performance.disk_read_speed[i] = list_to_add + Performance.disk_read_speed[i]     # "disk_read_speed" list has sub-lists and addition is performed for every sub-lists (for every disk).
                Performance.disk_write_speed[i] = list_to_add + Performance.disk_write_speed[i]   # "disk_write_speed" list has sub-lists and addition is performed for every sub-lists (for every disk).
            network_receive_speed_len = len(Performance.network_receive_speed)
            for i in range(network_receive_speed_len):
                Performance.network_receive_speed[i] = list_to_add + Performance.network_receive_speed[i]    # "network_receive_speed" list has sub-lists and addition is performed for every sub-lists (for every network card).
                Performance.network_send_speed[i] = list_to_add + Performance.network_send_speed[i]    # "network_send_speed" list has sub-lists and addition is performed for every sub-lists (for every network card).
            if MainGUI.radiobutton1005.get_active() == True:
                from Gpu import Gpu
                Gpu.fps_count = list_to_add + Gpu.fps_count                                       # "fps_count" list has no sub-lists and addition is performed in this way.


    # ----------------------- Called for applying settings for all opened tabs (since application start) without waiting update interval -----------------------
    def settings_gui_apply_settings_immediately_func(self):

        try:
            from MainGUI import Cpu
            Cpu.cpu_initial_func()
        except ImportError:
            pass

        try:
            from MainGUI import Ram
            Ram.ram_initial_func()
        except ImportError:
            pass

        try:
            from MainGUI import Disk
            Disk.disk_initial_func()
        except ImportError:
            pass

        try:
            from MainGUI import Network
            Network.network_initial_func()
        except ImportError:
            pass

        try:
            from MainGUI import Gpu
            Gpu.gpu_initial_func()
        except ImportError:
            pass

        try:
            from MainGUI import Sensors
            Sensors.sensors_initial_func()
        except ImportError:
            pass

        try:
            from MainGUI import Processes
            Processes.processes_initial_func()
        except ImportError:
            pass

        try:
            from MainGUI import Users
            Users.users_initial_func()
        except ImportError:
            pass

        try:
            from MainGUI import Startup
            Startup.startup_initial_func()
        except ImportError:
            pass

        try:
            from MainGUI import Services
            Services.services_initial_func()
        except ImportError:
            pass

        try:
            from MainGUI import System
            System.system_initial_func()
        except ImportError:
            pass

        MainGUI.main_gui_tab_loop_func()

        # Show/Hide Floating Summary Window by reading reset settings.
        from FloatingSummary import FloatingSummary
        # Floating Summary window is tried to be hidden in order to prevent opening a second window if default value for "show_floating_summary" is "1" and the Floating Summary window is already visible.
        try:
            FloatingSummary.window3001.hide()
        except AttributeError:
            pass
        # Shown Floating Summary window if default value of "show_floating_summary" is "1".
        if Config.show_floating_summary == 1:
            # Window has to be shown before running loop thread of the Floating Summary window. Because window visibility data is controlled to continue repeating "floating_summary_run_func" function.
            FloatingSummary.window3001.show()


    # ----------------------- Called for saving default main tab and performace tab sub-tab when "Remember last opened tabs" option is enabled -----------------------
    def settings_gui_default_tab_func(self):

        if MainGUI.radiobutton1.get_active() == True:
            Config.default_main_tab = 0
        elif MainGUI.radiobutton2.get_active() == True:
            Config.default_main_tab = 1
        elif MainGUI.radiobutton3.get_active() == True:
            Config.default_main_tab = 2
        elif MainGUI.radiobutton5.get_active() == True:
            Config.default_main_tab = 3
        elif MainGUI.radiobutton6.get_active() == True:
            Config.default_main_tab = 4
        elif MainGUI.radiobutton8.get_active() == True:
            Config.default_main_tab = 5

        if MainGUI.radiobutton1001.get_active() == True:
            Config.performance_tab_default_sub_tab = 0
        elif MainGUI.radiobutton1002.get_active() == True:
            Config.performance_tab_default_sub_tab = 1
        elif MainGUI.radiobutton1003.get_active() == True:
            Config.performance_tab_default_sub_tab = 2
        elif MainGUI.radiobutton1004.get_active() == True:
            Config.performance_tab_default_sub_tab = 3
        elif MainGUI.radiobutton1005.get_active() == True:
            Config.performance_tab_default_sub_tab = 4
        elif MainGUI.radiobutton1006.get_active() == True:
            Config.performance_tab_default_sub_tab = 5


    # ----------------------- Called for showing a warning dialog for resetting all settings -----------------------
    def settings_gui_reset_all_settings_warning_dialog(self):

        warning_dialog2001 = Gtk.MessageDialog(transient_for=self.window2001, title="", flags=0, message_type=Gtk.MessageType.WARNING,
        buttons=Gtk.ButtonsType.YES_NO, text=_tr("Do you want to reset all settings to defaults?"))
        warning_dialog2001.format_secondary_text("")
        self.warning_dialog2001_response = warning_dialog2001.run()
        warning_dialog2001.destroy()


# Generate object
SettingsGUI = SettingsGUI()


# System Monitoring Center

GTK3 and Python 3 based, system performance and usage monitoring tool.


<p align="center">
<a href="https://github.com/hakandundar34coding/system-monitoring-center/tags"><img alt="Platform (GNU/Linux)" src="https://img.shields.io/badge/platform-GNU/Linux-blue.svg"/></a>
<a href="https://github.com/hakandundar34coding/system-monitoring-center/tags"><img alt="GitHub tag (latest by date)" src="https://img.shields.io/github/v/tag/hakandundar34coding/system-monitoring-center"></a>
<a href="https://github.com/hakandundar34coding/system-monitoring-center/tags"><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/system-monitoring-center"></a>
<a href="https://github.com/hakandundar34coding/system-monitoring-center/tags"><img alt="Download System Monitoring Center" src="https://img.shields.io/sourceforge/dt/system-monitoring-center.svg" ></a>
<a href="https://github.com/hakandundar34coding/system-monitoring-center/tags"><img alt="GitHub all releases" src="https://img.shields.io/github/downloads/hakandundar34coding/system-monitoring-center/total"></a>
<a href="https://pypi.org/project/system-monitoring-center/"><img src="https://img.shields.io/badge/Visit-PyPI%20Page-b37840"/></a>
<a href="https://github.com/hakandundar34coding/system-monitoring-center/blob/master/Changes.md"><img src="https://img.shields.io/badge/View-Changelog-b37840"></a>
</p>


### Installation:
* System Monitoring Center is installable from PyPI as a Python package.
* Remove older versions (v1.8.0 and older).
* Install this dependency: ```mesa-utils (on some systems: glx-utils)```
* Option-1) Installing for current user account: ```pip install system-monitoring-center```
* Option-2) Installing for system-wide: ```sudo pip install system-monitoring-center```
  (This method can be used for preventing source code modifications.)
* First run:
  Run the application by using ```system-monitoring-center``` command.
  The application will prepare shortcut and GUI images automatically.
  If command is not found, restart the system and run the command again.


------------------

These dependencies are already installed on many systems:
```bash (>=4.4), dmidecode, iproute2, python3 (>=3.6), python3-cairo, python3-gi, python3-gi-cairo, util-linux (>=2.31)```

------------------


### Features:
* Detailed system performance and usage usage monitoring/managing features:
    * Monitoring CPU, RAM, Disk, Network, GPU hardware information/performance/usage
    * An always on top and semi-transparent floating summary window for performance monitoring
    * Monitoring and managing processes, users, startup applications and services (systemd)
    * Monitoring sensors and general system information
* Language support:
    * Brazilian Portuguese, Czech, English, Polish (initial), Turkish
    * More languages will be added if translations are provided by contributors
* Adapts to system theme
* Optimized for low CPU usage
* Free and open sourced


### Screenshots:
![System Monitoring Center](screenshots/cpu_tab_dark_system_theme.png)

![System Monitoring Center](screenshots/cpu_tab_white_system_theme.png)

![System Monitoring Center](screenshots/cpu_tab_per_core_dark_system_theme.png)

![System Monitoring Center](screenshots/network_tab_dark_system_theme.png)

![System Monitoring Center](screenshots/gpu_tab_dark_system_theme.png)

![System Monitoring Center](screenshots/sensors_tab_dark_system_theme.png)

![System Monitoring Center](screenshots/processes_list_view_dark_system_theme.png)

![System Monitoring Center](screenshots/startup_tab_dark_system_theme.png)

![System Monitoring Center](screenshots/services_tab_dark_system_theme.png)

![System Monitoring Center](screenshots/system_tab_dark_system_theme.png)


### Note:
* A simple FPS counter is shown on the GPU tab and may not be accurate in some situations.
* FPS counting does not continue when window is minimized.


Q:
  GDBus.Error:org.freedesktop.DBus.Error.ServiceUnknown: The name org.gnome.SettingsDaemon was not provided by any .service files

A:
  Restarting gnome-settings-daemon fixed it for me:

  gnome-settings-daemon --replace > /dev/null 2>&1 &

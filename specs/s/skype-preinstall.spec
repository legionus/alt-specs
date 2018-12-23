Name:     skype-preinstall
Version:  1.0
Release:  alt2
Summary:  Compatible layer for install official Skype package for OpenSUSE
License:  ALT-Public-Domain
Group:    Networking/Instant messaging
Packager: Andrey Cherepanov <cas@altlinux.org>
 
ExclusiveArch: %ix86
  
BuildRequires: libstdc++6
BuildRequires: alsa-plugins-pulse
BuildRequires: libpng12
BuildRequires: libpulseaudio
BuildRequires: libqt4-core
BuildRequires: libqt4-dbus
BuildRequires: libqt4-gui
BuildRequires: libqt4-network
BuildRequires: libqt4-webkit
BuildRequires: libqt4-xml
BuildRequires: libX11
BuildRequires: libXext
BuildRequires: libXScrnSaver
BuildRequires: libXv

# skype-4.3.0.37-suse.i586.rpm requires these
Requires: libqt4-x11 >= 4.6
Requires: libqt4 >= 4.6

Provides: libQtWebKit4
Provides: libasound_module_pcm_pulse.so
Provides: libpng12-0
Provides: libpulse0
Provides: xorg-x11-libXv
Provides: xorg-x11-libs

%description
%summary

%install
mkdir -p %buildroot%_libdir/%name
for lib in alsa-lib/libasound_module_conf_pulse.so \
	   libpng12.so.0 \
	   libpulse.so.0 \
	   libstdc++.so.6 \
	   libQtCore.so.4 \
	   libQtDBus.so.4 \
	   libQtGui.so.4 \
	   libQtNetwork.so.4 \
	   libQtWebKit.so.4 \
	   libQtXml.so.4 \
	   libX11.so.6 \
	   libXext.so.6 \
	   libXss.so.1 \
	   libXv.so.1
do 
    ln -s /usr/lib/$lib %buildroot%_libdir/%name/
done

%files
%_libdir/%name

%changelog
* Wed Oct 28 2015 Michael Shigorin <mike@altlinux.org> 1.0-alt2
- Added explicit R: libqt4 libqt4-x11 so rpminstall is enough

* Tue Sep 02 2014 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus

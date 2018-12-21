%define pear_name Event_Dispatcher

Name: pear-Event_Dispatcher
Version: 1.1.0
Release: alt1

Summary: Dispatch notifications using PHP callbacks

License: BSD License
Group: Development/Other
Url: http://pear.php.net/package/Event_Dispatcher

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Event_Dispatcher-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
The Event_Dispatcher acts as a notification dispatch table.
It is used to notify other objects of interesting things. This
information is encapsulated in Event_Notification objects. Client
objects register themselves with the Event_Dispatcher as observers of
specific notifications posted by other objects. When an event occurs,
an object posts an appropriate notification to the Event_Dispatcher.
The Event_Dispatcher dispatches a message to each registered
observer, passing the notification as the sole argument.

%prep
%setup -c

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_dir/Event
%pear_testdir/Event_Dispatcher/
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Wed Jul 27 2016 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version 1.1.0 (with rpmrb script)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus


%define pear_name Net_Dig

Name: pear-Net_Dig
Version: 0.1
Release: alt3

Summary: The PEAR::Net_Dig class should be a nice, friendly OO interface to the dig command

License: PHP 2.02
Group: Development/Other
Url: http://pear.php.net/package/Net_Dig

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/Net_Dig-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
The PEAR::Net_Dig class should be a nice, friendly OO interface to the dig
command

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
%pear_dir/Net
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus


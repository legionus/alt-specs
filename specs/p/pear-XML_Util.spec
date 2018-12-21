%define pear_name XML_Util

Name: pear-XML_Util
Version: 1.2.3
Release: alt1

Summary: XML utility class

License: PHP License
Group: Development/Other
Url: http://pear.php.net/package/XML_Util

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/XML_Util-%version.tar

BuildArchitectures: noarch

Requires: pear-core php5
BuildRequires: pear-core rpm-build-pear

%description
Selection of methods that are often needed when working with XML documents.
Functionality includes creating of attribute lists from arrays, creation of
tags, validation of XML names and more.

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
%pear_dir/XML
%pear_docdir/%pear_name/
%pear_testdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jan 09 2015 Pavel Isopenko <pauli@altlinux.org> 1.2.3-alt1
- new version XML_Util 1.2.3 (ALT #30632)

* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt3
- autorebuild for correct requires(pre) (see bug #16086)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt1
- initial build for ALT Linux Sisyphus


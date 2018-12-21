%define node_modules %_libexecdir/node_modules

Name: azure-sdk-for-node
Version: 0.6.1
Release: alt3
Summary: Windows Azure Client Library for node

Group: Development/Other
License: Apache-2.0
Url: http://github.com/WindowsAzure/azure-sdk-for-node

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires: npm node

%description
Windows Azure SDK for Node.js and Linux client toold.

%prep
%setup

%install
mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%node_modules/azure/
cp -a bin examples lib node_modules test package.json README.md %buildroot/%node_modules/azure/
rm -f %buildroot/%node_modules/azure/node_modules/sax/examples/switch-bench.js
rm -f %buildroot/%node_modules/azure/node_modules/sinon/build
rm -f %buildroot/%node_modules/azure/node_modules/sinon/step-tests
rm -f %buildroot/%node_modules/azure/node_modules/streamline/examples/misc/shebang.sh

ln -s "../lib/node_modules/azure/bin/azure" %buildroot/%_bindir/azure

%files
%_bindir/azure
%node_modules/azure

%changelog
* Wed Apr 03 2013 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt3
- Fix build with new node version

* Fri Jul 27 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.1-alt2
- merge upstream 6f210e9

* Wed Jul 11 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Fri Jun 29 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt1
- initial

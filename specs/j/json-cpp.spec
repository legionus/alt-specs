Name: json-cpp
Version: 3.4.0
Release: alt1

Summary: JSON for Modern C++ (c++11) ("single header file")

License: GPL
Group: Development/C++
Url: https://github.com/nlohmann/json

Packager: Pavel Vainerman <pv@altlinux.ru>
BuildArch: noarch

# Source: https://github.com/nlohmann/json/releases/download/v%{version}/json.hpp
Source: %name-%version.tar

#BuildRequires:

%description
There are myriads of JSON libraries out there, and each may even have its reason to exist. 
Our class had these design goals:
- intuitive syntax. 
- Trivial integration.
- Serious testing

%prep
%setup 

%build

%install
mkdir -p %buildroot%_includedir
mv -f json.hpp %buildroot%_includedir

%files
%_includedir/*.hpp

%changelog
* Mon Nov 26 2018 Pavel Vainerman <pv@altlinux.ru> 3.4.0-alt1
- new version

* Sun Mar 19 2017 Pavel Vainerman <pv@altlinux.ru> 2.1.1-alt1
- new version

* Tue Nov 08 2016 Pavel Vainerman <pv@altlinux.ru> 2.0.7-alt1
- new version

* Sun Oct 30 2016 Pavel Vainerman <pv@altlinux.ru> 2.0.6-alt0.1
- initial commit 

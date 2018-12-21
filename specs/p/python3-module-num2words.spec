%define  modulename num2words

Name:    python3-module-%modulename
Version: 0.5.8
Release: alt1

Summary: Modules to convert numbers to words. 42 --> forty-two
License: LGPL-2.1
Group:   Development/Python3
URL:     https://github.com/savoirfairelinux/num2words

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Tue Dec 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.8-alt1
- New version.

* Wed Jul 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.7-alt1
- New version.

* Fri Apr 06 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.6-alt1
- Initial build for Sisyphus

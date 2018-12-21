%define oname DistroDbMaker

%def_without python3

Name: python-module-%oname
Version: 0.021
Release: alt1
Summary: DistroDb Maker tools
License: LGPL2+
Group: Development/Python
Url: https://www.altlinux.org/Packaging_Automation/DistroDb

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

Conflicts: distrodb-utils < 0.21
Requires: python-module-rpm python-module-backports.lzma
#py_provides %oname

%description
%summary

%if_with python3
%package -n python3-module-%oname
Summary: DistroDb Maker tools
Group: Development/Python3
#py3_provides %oname

%description -n python3-module-%oname
%summary
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%_bindir/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Wed Dec 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.021-alt1
- new version

* Thu Jun 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.020-alt1
- new version

* Tue May 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.019-alt1
- new version

* Sat May 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.018-alt1
- new version

* Thu May 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.017-alt1
- new version

* Sat May 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1
- new version

* Thu Apr 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.015-alt1
- new version

* Sat Mar 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- added ocaml,erlang,nodejs

* Tue Mar 27 2018 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- added festival,mate,nagios,golang

* Mon Mar 26 2018 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- added gimp and cups

* Fri Mar 23 2018 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- added mono.raw

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- added shared-data.raw

* Wed Mar 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- cmake fixes

* Wed Mar 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- filtered out mageia multiarch dir

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- added filters

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- added java.raw

* Tue Mar 13 2018 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- exclude doc from texmf

* Sun Feb 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- mageia texlive support

* Fri Feb 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- alt support

* Mon Feb 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- xz list support

* Mon Feb 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- Initial build for Sisyphus

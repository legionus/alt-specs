%define dict_name dalf

Name: dict-%dict_name
Version: 0.1
Release: alt2

Summary: Dictionary: Dal's Russian Dictionary
Summary(ru_RU.KOI8-R): �������: �������� ������� ������ �������������� ����� ����
License: GPL
Group: Text tools
PreReq: dictd
Packager: Alexey Dyachenko <alexd@altlinux.ru>

Source0: %dict_name.dict.dz
Source1: %dict_name.index

BuildArch: noarch

%description
Dal's Russian Dictionary

%description -l ru_RU.KOI8-R
�������� ������� ������ �������������� ����� ����

%install
install -p -m644 -D %SOURCE0 %buildroot%_datadir/dictd/%dict_name.dict.dz
install -p -m644 -D %SOURCE1 %buildroot%_datadir/dictd/%dict_name.index


%files
%_datadir/dictd/%{dict_name}*

%changelog
* Wed Feb 04 2015 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2
- removed post/un in favor of filetrigger

* Sun Jun 03 2007 Slava Semushin <php-coder@altlinux.ru> 0.1-alt1.1
- NMU
- Fixed incomplete locale specification in Summary tag (#11840)
- Set packager tag to previous maintainer
- Spec cleanup:
  + s/BuildArchitectures/BuildArch/
  + s/$$RPM_BUILD_ROOT/%%buildroot/
  + Removed outdated Url tag
  + Removed one tab
  + Removed empty %%prep section
  + Use macros %%_sbindir instead of appropriate path

* Thu Jan 29 2004 Alexey Dyachenko <alexd@altlinux.ru> 0.1-alt1
- initial build

Name: ladspa-guitar-doc
Version: 1.0
Release: alt1
Summary: LADSPA guitar plugin family documentation and examples
Summary(ru_RU.KOI8-R): ������������ � ������� ��� ��������� �������� �������� LADSPA
License: GPL
Group: Sound
Url: http://quitte.de/dsp/
Packager: Mikhail Yakshin <greycat@altlinux.ru>
Source0: %name-%version.tar.bz2
BuildArchitectures: noarch

%description
Documentation contains all the developer's notes published on
project's homepage plus some good-sounding samples of ecasound chain
configs to try playing guitar live, including both hard and clean
modes.

%description -l ru_RU.KOI8-R
������������ �������� ��� ������� �������������, �������������� ��
��������� �������. � ������� �������� ��������� ������ ��������
�������� ������� ecasound ��� ���� �� ������ ������, ������� �
�������, � ������ ����.

%prep
%setup -q

%files
%doc *
 
%changelog
* Tue Sep 30 2003 Mikhail Yakshin <greycat@altlinux.org> 1.0-alt1
- Initial build for Sisyphus

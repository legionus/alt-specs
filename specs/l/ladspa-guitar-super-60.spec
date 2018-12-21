Name: ladspa-guitar-super-60
Version: 1.0
Release: alt1.1.qa1
Summary: LADSPA plugin to simulate Fender Super 60 amp
Summary(ru_RU.KOI8-R): ������ LADSPA ��� ��������� ��������� Fender Super 60 amp
License: GPL
Group: Sound
Url: http://quitte.de/dsp/
Packager: Mikhail Yakshin <greycat@altlinux.ru>
Source0: super-60.tar.gz
Patch: ladspa-guitar-super-60-options.patch.gz

# Automatically added by buildreq on Tue Sep 30 2003
BuildRequires: ladspa_sdk

%description
These LADSPA plugins, accompanied by some blurbs about motivation and
approach, mostly centered around (but not in the least confined to)
digital guitarist needs.

'super-60' is another effort to recreate the physical and electronic
spectral effects of an electric instrument amplifier, applying the
same methods as the predating 'unmatched' project. In short, it makes
a signal sound very much like it went through Fender Super 60 amp, bar
nonlinear effects and intra-cabinet reflection. Unlike traditional
convolution methods, it employs a 16th order IIR filter to emulate a
pre-recorded impulse response, resulting in realtime-compatible CPU
usage figures (4-8% on a ~500 MHz box).

%description -l ru_RU.KOI8-R
��� ������� LADSPA � �������� ������������� ��� ���� ���������
��������� (�� ������ �� ���������� ���).

'super-60' - ��� ���� ������� ������������� ���������� � �����������
������������ ������� ���������������� ���������, ��������� �� ��
������, ��� � � ������� 'unmatched'. ����� ������, �� ���������
������� ������� ���, ��� ���� �� �� ������ ����� ��������� Fender
Super 60, �� ������ ���������� �������� � ��������� ����� ������
���������. � ������� �� ������������ �������, ���� ������ ���������
IIR-������ 16��� ������� ��� �������� ����������� �������� ������, ���
��������� ������������ ���� � �������� ������� (4-8% �������� �� ~500
��� �������).

%prep
%setup -n super-60
%patch -p1

%build
%add_optflags %optflags_shared
export CFLAGS="%optflags"
%make_build

%install
%__install -D -m644 super-60.so %buildroot%_ladspa_path/super-60.so

%files
%_ladspa_path/*.so

%changelog
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0-alt1.1.qa1
- NMU: rebuilt for debuginfo.

* Mon Dec 22 2003 Mikhail Yakshin <greycat@altlinux.org> 1.0-alt1.1
- Fixed text relocations

* Tue Sep 30 2003 Mikhail Yakshin <greycat@altlinux.org> 1.0-alt1
- Initial build for Sisyphus

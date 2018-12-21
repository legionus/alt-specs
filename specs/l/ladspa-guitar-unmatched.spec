Name: ladspa-guitar-unmatched
Version: 1.0
Release: alt1.1.qa1
Summary: LADSPA plugin to simulate guitar amp cabinet
Summary(ru_RU.KOI8-R): ������ LADSPA ��� ��������� ��������� ��������
License: GPL
Group: Sound
Url: http://quitte.de/dsp/
Packager: Mikhail Yakshin <greycat@altlinux.ru>
Source0: unmatched.tar.gz
Patch: ladspa-guitar-unmatched-options.patch.gz

# Automatically added by buildreq on Tue Sep 30 2003
BuildRequires: ladspa_sdk

%description
These LADSPA plugins, accompanied by some blurbs about motivation and
approach, mostly centered around (but not in the least confined to)
digital guitarist needs.

'unmatched' is a simple effort to emulate certain aspects of the tone 
of a real musical instrument amplifier, in real time.

%description -l ru_RU.KOI8-R
��� ������� LADSPA � �������� ������������� ��� ���� ���������
��������� (�� ������ �� ���������� ���).

'unmatched' - ������� ������� ������������ ��������� ������� ������
���������� ��������� ��������� � �������� �������.

%prep
%setup -n unmatched
%patch -p1

%build
%add_optflags %optflags_shared
export CFLAGS="%optflags"
%make_build 

%install
%__install -D -m644 unmatched.so %buildroot%_ladspa_path/unmatched.so

%files
%_ladspa_path/*.so

%changelog
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0-alt1.1.qa1
- NMU: rebuilt for debuginfo.

* Sat Nov 22 2003 Mikhail Yakshin <greycat@altlinux.org> 1.0-alt1.1
- Fixed text relocations

* Tue Sep 30 2003 Mikhail Yakshin <greycat@altlinux.org> 1.0-alt1
- Initial build for Sisyphus

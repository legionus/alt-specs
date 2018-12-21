Packager: Repocop Q. A. Robot <repocop@altlinux.org>
Name: slsnif
Version: 0.4.4
Release: alt1.1.qa1

Summary: %name is a serial line sniffer
License: GPL
Group: System/Kernel and hardware
URL: http://www.dakotacom.net/~ymg/software.html
Source: %name-%version.tar.gz
# This comment added for moving non-ASCII directives behind first 256 bytes
Summary(ru_RU.KOI8-R): %name ��� ������� ��� ���������� �� ����������������� �������

%description
%name is a serial line sniffer. It listens to the specified serial port and logs
all data coming through it. %name works transparently for both the device connected
to the serial port and the controlling software for this device.

%description -l ru_RU.KOI8-R
������� ��� ���������� �� ����������������� �������. %name ������� ������������ ����������������
���� � ���������� � ������ ��� ������, ������� ����� ���� ��������. %name �������� ��� � �����������,
�������������� � �����, ��� � � ����������� ���� ����������� ����������� ������������.

%prep
%setup -c

%build
make -f gcc.mak

%install
make -f gcc.mak DESTDIR=%buildroot install

%files
%_bindir/%name
%_docdir/%name-%version/README
# The package does not own its own docdir subdirectory.
# The line below is added by repocop to fix this bug in a straightforward way. 
# Another way is to rewrite the spec to use relative doc paths.
%dir %_docdir/slsnif-%version 

%changelog
* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.4.4-alt1.1.qa1
- NMU: rebuilt for updated dependencies.

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1.1
- NMU (by repocop): the following fixes applied:
  * docdir-is-not-owned for slsnif

* Sat Feb 12 2005 Mike Matveev <matveev@altlinux.ru> 0.4.4-alt1
- written spec-file satisfied ALT Specfile Conventions

## EOF ##

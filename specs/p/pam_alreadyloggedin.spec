Name: pam_alreadyloggedin
Version: 0.3.2
Release: alt2

%def_without libpam
%def_with    libpam0
%def_without libpam2

%define pamconfdir   %_sysconfdir/pam.d
%define pamlibdir    /lib/security
%define mydocdir     %_docdir/%name-%version
%define examples_dir %mydocdir/examples

Summary: Skip password authorization if user is already logged in
License: relaxed BSD and (L)GPL-compatible
Group: System/Base
Url: http://ilya-evseev.narod.ru/posix/%name
Source: %url/%name-%version.tar.gz

%if_with libpam
BuildPreReq: libpam-devel
%endif
%if_with libpam0
BuildPreReq: libpam0-devel
%endif
%if_with libpam2
BuildPreReq: libpam2-devel
%endif

Summary(ru_RU.KOI8-R): ���� � ������� ��� ������, ���� ��� �������� ���� � ������ �������

%description
Based on the appropriate module from FreeBSD project source tree,
%name is a PAM module which allows you to skip
authorization stuff (like password entering, etc.),
if you are already logged in on the another console.
See using example in %pamconfdir/login.sso file.

%description -l ru_RU.KOI8-R
%name �������� ������� PAM, ������� ��������� ������������
���������� ���� ������ ��� ����� � �������,
���� ���� ������������ ��� ��ۣ� � ������� � ������ �������.

������ ������ �� �������� �������������� ���������� ��� �����������;
������ �������� PAM ��� ��� ����������� �������� � ��������
%examples_dir.

%prep
%setup -q -c

%build
%make_build

%install
%make_install install FAKEROOT=%buildroot MAN8DIR=%_man8dir
install -pD -m644 login.sso %buildroot%examples_dir/login

%ifdef add_findprov_lib_path
%add_findprov_lib_path %pamlibdir
%endif

%files
%pamlibdir/%name.so
%examples_dir/login
%exclude %pamconfdir/login.sso
%_man8dir/%name.8*
# The package does not own its own docdir subdirectory.
# The line below is added by repocop to fix this bug in a straightforward way. 
# Another way is to rewrite the spec to use relative doc paths.
%dir %_docdir/pam_alreadyloggedin-%version 
%dir %examples_dir

%changelog
* Mon Sep 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.2-alt2
- Fixed spec to allow any man page compression

* Tue Apr 23 2013 Repocop Q. A. Robot <repocop@altlinux.org> 0.3.2-alt1.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * docdir-is-not-owned for pam_alreadyloggedin

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.3.2-alt1.qa1
- NMU: rebuilt for updated dependencies.

* Wed Nov 22 2006 Ilya Evseev <evseev@altlinux.ru> 0.3.2-alt1
- prevent gcc4 stack protection problem: http://wiki.sisyphus.ru/devel/gcc4
- include syslog.h to sources

* Fri Oct  7 2005 Ilya G. Evseev <evseev@altlinux.ru> 0.3.1-alt1
- bugfix in 0.3.1: explicitly include syslog headers in debug mode.
- handle libpam-devel alternatives in Sisyphus,
  use "rpmbuild --with libpam" for getting old functionality.
- new feature in 0.3.1 makefile: added targets "archive", "rpm".

* Sun Nov 28 2004 Ilya G. Evseev <evseev@altlinux.ru> 0.3-alt1
- version 0.3: patch from Luca Benini <lbenini@csr.unibo.it>
  for skipping some checks no more actual for Linux
- specfile warning about unused policy installed in %pamconfdir

* Wed Aug  4 2004 Ilya G. Evseev <evseev@altlinux.ru> 0.2-alt4
- added add_findprov_lib_path macro
- login.sso is moved from /etc/pam.d to docdir/examples,
  comments are no more needed.

* Tue Jul  6 2004 Ilya G. Evseev <evseev@altlinux.ru> 0.2-alt3
- fixups in login.sso for preventing invalid RPM requirements
- source archive format is changed from ZIP to tar.gz

* Fri Jul  2 2004 Ilya G. Evseev <evseev@altlinux.ru> 0.2-alt2
- specfile cleanups before adding to ALTLinux Sisyphus repository
- added russian summary and description

* Wed Jan 28 2004 Ilya G. Evseev <ilya_evseev@mail.ru> 0.2-1
- Initial build, based on the FreeBSD's module version 0.2

## EOF ##

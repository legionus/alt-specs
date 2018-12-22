Name: wf
Version: 0.41
Release: alt1.qa1

Summary: Simple word frequency counter
License: GPL-2.0-only
Group: Text tools
Url: http://www.async.com.br/~marcelo/wf/
Source: %name-%version.tar
Packager: Evgenii Terechkov <evg@altlinux.org>

%description
wf scans a text file and counts the frequency of words through the whole text

%prep
%setup

%build
%autoreconf
%configure
make

%install
%makeinstall

%files
%_bindir/%name
%_man1dir/%name.*

%doc AUTHORS NEWS README TODO ChangeLog

%changelog
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.41-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Mar 29 2009 Terechkov Evgenii <evg@altlinux.ru> 0.41-alt1
- Initial build for ALT Linux Sisyphus

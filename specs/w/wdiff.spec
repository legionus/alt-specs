Name: wdiff
Version: 1.2.2
Release: alt1.1
Summary: Comparing files on a word per word basis
License: GPL
Group: Text tools
Url: http://www.gnu.org/software/wdiff/
Source: %name-%version.tar.gz

# Needs for check
BuildRequires: screen
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
The program wdiff is a front end to diff for comparing files on a word
per word basis. A word is anything between whitespace. This is useful
for comparing two texts in which a few words have been changed and for
which paragraphs have been refilled. It works by creating two temporary
files, one word per line, and then executes diff on these files. It
collects the diff output and uses it to produce a nicer display of word
differences between the original files.

%prep
%setup

%build
#autoreconf
%configure --enable-experimental
%make_build

%check
%make check

%install
%makeinstall
%find_lang "%name.*"

%files -f %name.*.lang
%doc ABOUT-NLS AUTHORS BACKLOG ChangeLog INSTALL NEWS README THANKS TODO
%_bindir/*
%_man1dir/*
%_infodir/*

%changelog
* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1.1
- NMU: added BR: texinfo

* Mon May 12 2014 Fr. Br. George <george@altlinux.ru> 1.2.2-alt1
- Autobuild version bump to 1.2.2

* Sun Mar 31 2013 Fr. Br. George <george@altlinux.ru> 1.2.1-alt1
- Autobuild version bump to 1.2.1

* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 1.1.2-alt1
- Autobuild version bump to 1.1.2

* Wed Jan 11 2012 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1
- Autobuild version bump to 1.1.0

* Fri Sep 16 2011 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Autobuild version bump to 1.0.1

* Fri Sep 09 2011 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1
- Autobuild version bump to 1.0.0
- Fix check section

* Tue May 31 2011 Fr. Br. George <george@altlinux.ru> 0.6.5-alt1
- Initial build from scratch

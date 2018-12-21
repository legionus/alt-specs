Name: hashdeep
Version: 4.4
Release: alt1

Summary: Compute message digests on an arbitrary number of files
License: Public domain, GPLv2 (Tiger)
Group: File tools

Url: https://github.com/jessek/hashdeep
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++

Provides: md5deep = %version
Obsoletes: md5deep

Summary(pl.UTF-8): Obliczanie skrótów MD5 dla dowolnej liczby plików

%description
This is md5deep, a set of cross-platform tools to computer
hashes, or message digests, for any number of files while
optionally recursively digging through the directory structure.
It can also take a list of known hashes and display the filenames
of input files whose hashes either do or do not match any of the
known hashes.

This version supports MD5, SHA-1, SHA-256, Tiger, and Whirlpool
hashes.

md5deep is similar to the md5sum program found in the GNU Coreutils
package, but has the following additional features:
- Recursive operation - md5deep is able to recursive examine an entire
  directory tree. That is, compute the MD5 for every file in a directory
  and for every file in every subdirectory.
- Time estimation - md5deep can produce a time estimate when it's
  processing very large files.
- Comparison mode - md5deep can accept a list of known hashes and
  compare them to a set of input files. The program can display either
  those input files that match the list of known hashes or those that do
  not match.

%description -l pl.UTF-8
md5deep to wieloplatformowy program do obliczania skrótów MD5 dla
dowolnej liczby plików. Program działa pod Windows, Linuksem, FreeBSD,
OS X, Solarisem i powinien działać na większości innych platform.
md5deep jest podobny do programu md5sum z pakietu GNU Coreutils, ale
ma następujące dodatkowe możliwości:
- praca rekurencyjna - md5deep może rekurencyjnie sprawdzać całe
  drzewo katalogów, obliczając MD5 dla każdego pliku w katalogu oraz dla
  każdego pliku we wszystkich jego podkatalogach;
- szacowanie czasu - md5deep może pokazywać oszacowania czasu trwania
  operacji przy przetwarzaniu bardzo dużych plików;
- tryb porównywania - md5deep może dostać listę znanych skrótów i
  porównywać je ze zbiorem plików wejściowych; program może wypisać te
  pliki, które pasują do listy znanych skrótów lub te, które nie pasują.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog FILEFORMAT NEWS README TODO
%_bindir/*
%_man1dir/*

%changelog
* Tue May 27 2014 Michael Shigorin <mike@altlinux.org> 4.4-alt1
- 4.4 (github buid, thanks Maxim Suhanov)

* Tue May 27 2014 Michael Shigorin <mike@altlinux.org> 4.3-alt1
- new version (watch file uupdate)

* Sat Apr 21 2012 Michael Shigorin <mike@altlinux.org> 4.1-alt1
- 4.1

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 3.9.2-alt1
- 3.9.2

* Fri Jan 21 2011 Michael Shigorin <mike@altlinux.org> 3.7-alt1
- 3.7 (thanks force@)

* Sat Feb 20 2010 Michael Shigorin <mike@altlinux.org> 3.5.1-alt1
- 3.5.1

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 3.3-alt1
- 3.3
- removed obsolete patch
- spec cleanup

* Fri Aug 24 2007 Michael Shigorin <mike@altlinux.org> 1.13-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)
- replaced PLD makefile patch with updated one based on it
- dropped special handling of manpage aliases as that would
  be fixed back to symlinks at the post-build stage anyways
- License: Public domain (see manpage)

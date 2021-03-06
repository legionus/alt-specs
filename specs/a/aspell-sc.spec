# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 1.0

%define languageenglazy Sardinian
%define languagecode sc
%define lc_ctype sc_IT

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.50.1
Release:       alt2_16
Group:         Text tools
#Source:        ftp://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell-%{languagecode}-%{src_ver}.tar.bz2
Source:        ftp://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell5-%{languagecode}-%{src_ver}.tar.bz2
URL:           http://aspell.net/
License:	   GPL
Provides: spell-%{languagecode}


BuildRequires: aspell >= 0.50
Requires:      aspell >= 0.50

# Mageia Stuff
Requires:      locales-%{languagecode}
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}

Autoreqprov:   no
Source44: import.info

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
#%setup -q -n %{name}-%{src_ver}
%setup -q -n aspell5-%{languagecode}-%{src_ver}

%build

# don't use configure macro
./configure

%make

%install
%makeinstall_std

#mv -f README README.%{languagecode}
chmod 644 Copyright README* doc/*

%files
%doc README* Copyright doc/*
%{_libdir}/aspell*/*
%{_datadir}/aspell/*


%changelog
* Tue Oct 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt2_16
- fixed rpm Group:

* Sat Jun 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.50.1-alt1_16
- update by mgaimport


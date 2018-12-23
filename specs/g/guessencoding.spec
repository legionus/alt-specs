# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:             guessencoding
Version:          1.4
Release:          alt2_15jpp8
Summary:          Guess encoding of files and return configured reader
Group:            Development/Other
License:          Apache-2.0
URL:              http://docs.codehaus.org/display/GUESSENC/
# svn export http://svn.codehaus.org/guessencoding/tags/guessencoding-1.4/
# tar caf guessencoding-1.4.tar.gz guessencoding-1.4
Source0:          %{name}-%{version}.tar.gz
# Comment out wagon-webdav extension as it is not needed in Fedora
Patch0:           guessencoding-webdav.patch
BuildArch:        noarch

BuildRequires:    maven-local

%if 0%{?fedora} >= 20 || 0%{?rhel} >= 7
%else
Requires:         java
%endif
Requires:         jpackage-utils
Source44: import.info

%description
The purpose of this library is to "guess" the encoding of files, and retrieve
a reader that is properly configured to use the right encoding as guessed.
The library is able to recognize the various Unicode encoding variants:

    * UTF-8
    * UTF-16LE - Low Endian
    * UTF-16BE - Big Endian
    * UTF-32

If a Unicode encoding isn't recognized, it's an 8-bit encoding. If the 8-bit
encoding is not US-ASCII, the default platform 8-bit encoding is assumed
whatever it is. However, the library cannot guess between different 8-bit
encodings. Only statistical analysis, n-grams and similar techniques specific
to each language used in those files can help guessing the encoding, but this
is not supported by the library.


%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch:        noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q
%patch0 -p1 -b .webdav


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc


%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_15jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_14jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_13jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_4jpp7
- new version


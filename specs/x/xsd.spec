Group: Development/Tools
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
%define fedora 28
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: xsd
Version: 4.0.0
Release: alt2_25
Summary: W3C XML schema to C++ data binding compiler
# Exceptions permit otherwise GPLv2 incompatible combination with ASL 2.0
License: GPLv2 with exceptions and ASL 2.0  
URL: http://www.codesynthesis.com/products/xsd/
Source0: http://www.codesynthesis.com/download/xsd/4.0/xsd-%{version}+dep.tar.bz2

# Sent suggestion to upstream via e-mail 20090707
# http://anonscm.debian.org/cgit/collab-maint/xsd.git/tree/debian/patches/0001-xsd_xsdcxx-rename.patch
Patch0: %{name}-3.3.0-xsdcxx-rename.patch

# Fix bug in C++/Parser Expat Support
# http://codesynthesis.com/pipermail/xsd-users/2015-October/004705.html
Patch1: %{name}-Fix_bug_C++_Parser_Expat_Support.patch

# Remove tests for character reference values unsupported by Xerces-C++ 3.2
# https://anonscm.debian.org/cgit/collab-maint/xsd.git/diff/debian/patches/0110-xerces-c3.2.patch?id=442e98604d4158dae11056c4f94aaa655cb480fa
Patch2: %{name}-xerces_3-2.patch

BuildRequires: m4, libxerces-c-devel, libcutl-devel, gcc-c++
%if 0%{?rhel}
BuildRequires: boost148-devel
Requires: boost148
%else
BuildRequires: boost-complete
%endif
Source44: import.info

%description
CodeSynthesis XSD is an open-source, cross-platform W3C XML Schema to
C++ data binding compiler. Provided with an XML instance specification
(XML Schema), it generates C++ classes that represent the given
vocabulary as well as parsing and serialization code.
You can then access the data stored in XML using types and functions
that semantically correspond to your application domain rather than
dealing with intricacies of reading and writing XML.

%package   doc
Group: Documentation
BuildArch: noarch
Summary:   API documentation files for %{name}

%description    doc
This package contains API documentation for %{name}.

%prep
%setup -q -n xsd-%{version}+dep
%patch0 -p0
%patch1 -p0
%patch2 -p0

##Unbundle libcutl
rm -rf libcutl

%build
%if 0%{?rhel} < 7
%{!?__global_ldflags: %global __global_ldflags -Wl,-z,relro}
%endif
%make_build verbose=1 CXX=g++ CC=gcc CXXFLAGS="$RPM_OPT_FLAGS -fPIC -pie -Wl,-z,now" LDFLAGS="%{__global_ldflags} -fPIC -pie -Wl,-z,now" BOOST_LINK_SYSTEM=y EXTERNAL_LIBCUTL=y

%install
rm -rf apidocdir

%makeinstall_std LDFLAGS="%{__global_ldflags}" install_prefix=$RPM_BUILD_ROOT%{_prefix} \
 install_bin_dir=$RPM_BUILD_ROOT%{_bindir} install_man_dir=$RPM_BUILD_ROOT%{_mandir} EXTERNAL_LIBCUTL=y BOOST_LINK_SYSTEM=y

# Split API documentation to -doc subpackage.
mkdir -p apidocdir
mv $RPM_BUILD_ROOT%{_datadir}/doc/xsd/*.{xhtml,css} apidocdir/
mv $RPM_BUILD_ROOT%{_datadir}/doc/xsd/cxx/ apidocdir/
mv $RPM_BUILD_ROOT%{_datadir}/doc/xsd/ docdir/

# Convert to utf-8.
for file in docdir/NEWS; do
    mv $file timestamp
    iconv -f ISO-8859-1 -t UTF-8 -o $file timestamp
    touch -r timestamp $file
done

# Rename binary to xsdcxx to avoid conflicting with mono-web package.
# Sent suggestion to upstream via e-mail 20090707
# they will consider renaming in 4.0.0
mv $RPM_BUILD_ROOT%{_bindir}/xsd $RPM_BUILD_ROOT%{_bindir}/xsdcxx
mv $RPM_BUILD_ROOT%{_mandir}/man1/xsd.1 $RPM_BUILD_ROOT%{_mandir}/man1/xsdcxx.1

# Remove duplicate docs.
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/libxsd

# Remove Microsoft Visual C++ compiler helper files.
rm -rf $RPM_BUILD_ROOT%{_includedir}/xsd/cxx/compilers

# Remove redundant PostScript files that rpmlint grunts about not being UTF8
# See: https://bugzilla.redhat.com/show_bug.cgi?id=502024#c27
# for Boris Kolpackov's explanation about those
find apidocdir -name "*.ps" | xargs rm -f
# Remove other unwanted crap
find apidocdir -name "*.doxygen" \
            -o -name "makefile" \
            -o -name "*.html2ps" | xargs rm -f

##Test failed on EPEL6 due to "bad" xerces-c
##http://codesynthesis.com/pipermail/xsd-users/2015-October/004696.html
##https://bugzilla.redhat.com/show_bug.cgi?id=1270978
%if 0%{?fedora} || 0%{?rhel} >= 7
%check
make -j 1 test EXTERNAL_LIBCUTL=y BOOST_LINK_SYSTEM=y
%endif

%files
%doc docdir/README docdir/NEWS docdir/FLOSSE
%doc --no-dereference docdir/GPLv2 docdir/LICENSE
%{_bindir}/xsdcxx
%{_mandir}/man1/xsdcxx.1*
%{_includedir}/xsd/

%files doc
%doc docdir/README docdir/NEWS docdir/FLOSSE
%doc --no-dereference docdir/GPLv2 docdir/LICENSE
%doc apidocdir/*

%changelog
* Mon Dec 10 2018 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt2_25
- update to new release by fcimport

* Thu Jul 05 2018 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt2_23
- use boost-complete

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt1_23
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt1_20
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt1_15
- update to new release by fcimport

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.3.0-alt2_16.qa1
- NMU: rebuilt with boost 1.57.0 -> 1.58.0.

* Mon Mar 09 2015 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt2_16
- moved to Sisyphus by request of mike@

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_16
- update to new release by fcimport

* Tue Apr 30 2013 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_15
- initial fc import


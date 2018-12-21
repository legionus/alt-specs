%define _unpackaged_files_terminate_build 1
#
#   - Regexp::Assemble -
#   This spec file was automatically generated by cpan2rpm [ver: 2.028]
#   (ALT Linux revision)
#   The following arguments were used:
#       '--packager=Igor Vlasenko <viy@altlinux.ru>' http://search.cpan.org/CPAN/authors/id/D/DL/DLAND/Regexp-Assemble-0.35.tar.gz
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Regexp-Assemble
%define m_distro Regexp-Assemble
%define m_name Regexp::Assemble
%define m_author_id unknown
%define _enable_test 1

Name: perl-Regexp-Assemble
Version: 0.38
Release: alt1

Summary: Assemble multiple Regular Expressions into a single RE

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Igor Vlasenko <viy@altlinux.ru>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/R/RS/RSAVAGE/%{module}-%{version}.tgz

# Automatically added by buildreq on Wed May 30 2012
# optimized out: perl-Devel-Symdump perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-devel
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
Regexp::Assemble takes an arbitrary number of regular expressions
and assembles them into a single regular expression (or RE) that
matches all that the individual REs match.

As a result, instead of having a large list of expressions to loop
over, a target string only needs to be tested against one expression.
This is interesting when you have several thousand patterns to deal
with. Serious effort is made to produce the smallest pattern possible.

It is also possible to track the original patterns, so that you can
determine which, among the source patterns that form the assembled
pattern, was the one that caused the match to occur.

You should realise that large numbers of alternations are processed
in perl's regular expression engine in O(n) time, not O(1). If you
are still having performance problems, you should look at using a
trie. Note that Perl's own regular expression engine will implement
trie optimisations in perl 5.10 (they are already available in
perl 5.9.3 if you want to try them out). `Regexp::Assemble' will
do the right thing when it knows it's running on a a trie'd perl.
(At least in some version after this one).

Some more examples of usage appear in the accompanying README. If
that file isn't easy to access locally, you can find it on a web
repository such as
http://search.cpan.org/dist/Regexp-Assemble/README or
http://cpan.uwinnipeg.ca/htdocs/Regexp-Assemble/README.html.

%prep
%setup -q -n %{module}-%{version}
#sed -i -e 's,^=item \([1-8]\)$,=item NUMBER is \1,' Assemble.pm
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changelog.ini Changes README TODO examples
%perl_vendor_privlib/Regexp/*

%changelog
* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- automated CPAN update

* Wed Apr 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- automated CPAN update

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.35-alt2
- fixed pod

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- initial build for ALT Linux Sisyphus


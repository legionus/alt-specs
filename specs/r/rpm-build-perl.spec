%def_with bootstrap

Name: rpm-build-perl
Version: 0.84
Release: alt13

Summary: RPM helper scripts to calculate Perl dependencies
License: GPL
Group: Development/Other

URL: %CPAN %name
Source: %name-%version.tar.gz

# Automatically added by buildreq on Thu Nov 17 2011
BuildRequires: perl-Encode-JP perl-Encode-KR perl-Filter perl-Try-Tiny perl-devel

%if_with bootstrap
BuildArch: noarch
%endif

%description
These herlper scripts will look at perl source files in your package,
and will use this information to generate automatic Requires and Provides
tags for the package.

%prep
%setup
%if_with bootstrap
rm -r ConstOptree
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install INSTALLSCRIPT=%_rpmlibdir INSTALLVENDORSCRIPT=%_rpmlibdir
%if_with bootstrap
    mv %buildroot%perl_vendor_privlib/fake.pm %buildroot%_rpmlibdir/
%else
    mv %buildroot%perl_vendor_archlib/fake.pm %buildroot%_rpmlibdir/
%endif

mkdir -p %buildroot%_rpmmacrosdir
install -pm644 perl5-alt-rpm-macros %buildroot%_rpmmacrosdir/perl5
install -pm644 macros.env %buildroot%_rpmmacrosdir/perl5.env

%files
%doc README.ALT
%_rpmlibdir/perl.req
%_rpmlibdir/perl.req.files
%_rpmlibdir/perl.prov
%_rpmlibdir/perl.prov.files
%_rpmlibdir/perl.clean
%_rpmlibdir/fake.pm
%if_with bootstrap
%dir %perl_vendor_privlib/B
%perl_vendor_privlib/B/Walker.pm
%perl_vendor_privlib/B/PerlReq.pm
%perl_vendor_privlib/B/Clobbers.pm
%dir %perl_vendor_privlib/PerlReq
%perl_vendor_privlib/PerlReq/Utils.pm
%else
%dir %perl_vendor_archlib/B
%perl_vendor_archlib/B/Walker.pm
%perl_vendor_archlib/B/ConstOptree.pm
%perl_vendor_archlib/B/PerlReq.pm
%perl_vendor_archlib/B/Clobbers.pm
%dir %perl_vendor_autolib/B
%dir %perl_vendor_autolib/B/ConstOptree
%perl_vendor_autolib/B/ConstOptree/ConstOptree.so
%dir %perl_vendor_archlib/PerlReq
%perl_vendor_archlib/PerlReq/Utils.pm
%endif
%config %_rpmmacrosdir/perl5
%config %_rpmmacrosdir/perl5.env

%changelog
* Sun Dec 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.84-alt13
- enabled '.' in INC for perl 5.26 for compatibility
- still bootstrap for perl 5.26

* Fri Nov 24 2017 Igor Vlasenko <viy@altlinux.ru> 0.84-alt12
- bootstrap for perl 5.26

* Sun Feb 12 2017 Igor Vlasenko <viy@altlinux.ru> 0.84-alt11.1
- unbootstrap after rebuild with new perl 5.24.1

* Fri Jan 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.84-alt11
- bootstrap for perl 5.24

* Sat Nov 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.84-alt10
- support for package FOO VERSION in perl.prov

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.84-alt9
- support for Moo && Mouse

* Wed Apr 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.84-alt8
- support of bad xs in perl-optimizer && perl 5.22

* Thu Dec 17 2015 Igor Vlasenko <viy@altlinux.ru> 0.84-alt7.1
- unbootstrap

* Sat Nov 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.84-alt7
- support for perl 5.22 in B::PerlReq, B::Walker
- bootstrap for perl 5.22

* Fri Nov 13 2015 Igor Vlasenko <viy@altlinux.ru> 0.84-alt6
- a fix in B::Walker
- bootstrap

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.84-alt5
- bootstrap for perl update to 5.20.1

* Sat May 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.84-alt4
- better Module::Build recognition

* Wed Sep 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.84-alt3
- added exceptions for incorrect versions in RequiresPerl.

* Wed Aug 21 2013 Vladimir Lettiev <crux@altlinux.ru> 0.84-alt2
- unbootstrap

* Tue Aug 20 2013 Vladimir Lettiev <crux@altlinux.ru> 0.84-alt1
- Patch for B::Walker from #RT85411 (for perl > 5.17.5)
- implemented bootstrap to build noarch rpm-build-perl when perl API changed

* Wed Jul 31 2013 Igor Vlasenko <viy@altlinux.ru> 0.83-alt1
- Module::Build::Tiny support

* Fri Mar 08 2013 Dmitry V. Levin <ldv@altlinux.org> 0.82-alt2
- Relocated rpm macro files to %%_rpmmacrosdir/.

* Sat Sep 29 2012 Alexey Tourbin <at@altlinux.ru> 0.82-alt1
- B/ConstOptree.pm: new module, implements optree constant folding
  for $^O, $^V, and $] variables by installing custom PL_check hooks
- B/PerlReq.pm: now handles if.pm import routine

* Mon Sep 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.81-alt1
- updated test suite for perl-5.16

* Sat Nov 19 2011 Alexey Tourbin <at@altlinux.ru> 0.80-alt1
- B/PerlReq.pm: IO::File->new(\$var, ...) requires PerlIO::scalar

* Fri Nov 18 2011 Alexey Tourbin <at@altlinux.ru> 0.79-alt1
- B/PerlReq.pm: unify func/method processing via entersub
- B/PerlReq.pm: improved import method handling with list args
- B/PerlReq.pm: improved 'my $_' handler introduced in 0.78
- B/PerlReq.pm: stacked filetests require perl >= 5.10
- B/PerlReq.pm: treat Try::Tiny::try() like eval

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 0.78-alt1
- MANIFEST: added perl.clean

* Thu Nov 10 2011 Alexey Tourbin <at@altlinux.ru> 0.77-alt1
- PerlReq/Utils.pm: handle quoted-string versions by upgrading them
  to version.pm object, according to post-perl-5.8 rules
- B/PerlReq.pm: handle "use parent" import routine like that of "use base"
- B/PerlReq.pm: recognize and make deps on perl-5.10 syntactic features

* Fri Oct 21 2011 Alexey Tourbin <at@altlinux.ru> 0.76-alt1
- updated test suite for perl-5.14
- B/Walker.pm: invoke optree handlers only with non-zero line number,
  to ignore the code generated by PERL5OPT and command line switches
- perl.clean: factored from /usr/lib/rpm/brp-cleanup
- perl.clean: do not die on non-emtpy *.bs files
- perl.clean: also remove perllocal.pod files

* Thu Oct 06 2011 Alexey Tourbin <at@altlinux.ru> 0.75-alt1
- perl.{req,prov}.files: ignore */auto/share/{dist,module}/*
- B/PerlReq.pm: bumped minimum autodep perl version 5.6 -> 5.10

* Sat Feb 12 2011 Alexey Tourbin <at@altlinux.ru> 0.74-alt1
- B/PerlReq.pm: added warnings.pm to @Skip list

* Mon Nov 15 2010 Vladimir Lettiev <crux@altlinux.ru> 0.73-alt2
- fixed fatal error in walk_gv() when method CV return not B::CV class
  object (Closes: #24564)

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 0.73-alt1
- updated for perl-5.12:
- perl.req, perl.prov: relax dependency on Pod::Usage
- perl.prov: use plain eval insted of Safe->reval
- perl.prov: \Q stopped working without closing \E
- macros: removed UNINST=undef
- macros: removed OTHERLDFLAGS='-lperl -lpthread'
- macros: removed INSTALLMAN1DIR= and INSTALLMAN3DIR=
- macros: removed %%perl_vendor_man1dir and %%perl_vendor_man3dir

* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 0.72-alt1
- B/PerlReq.pm: implemented support for Moose::with()

* Sun Sep 27 2009 Alexey Tourbin <at@altlinux.ru> 0.71-alt1
- PerlReq/Utils.pm: fixed RPM_PERL_LIB_PATH for whitespaces (ALT#21701)

* Mon May 11 2009 Alexey Tourbin <at@altlinux.ru> 0.70-alt1
- B/Walker.pm: new module, implements optree traversal
- B/Clobbers.pm: new experimental module, for checking global variables
- PerlReq/Utils.pm: updated version formatting algorithm for better precision;
  the most general version format for rpm dependencies is now d.ddd.ddd

* Tue Mar 24 2009 Alexey Tourbin <at@altlinux.ru> 0.6.8-alt3
- macros (_perl_vendor_check_dso): disabled this check

* Tue Mar 24 2009 Alexey Tourbin <at@altlinux.ru> 0.6.8-alt2
- macros (_perl_vendor_check_dso): gcc -Wl,--no-as-needed

* Fri May 09 2008 Alexey Tourbin <at@altlinux.ru> 0.6.8-alt1
- perl.prov: try to detect block-level packages, fixes MP3/Tag.pm version

* Sat Mar 01 2008 Alexey Tourbin <at@altlinux.ru> 0.6.7-alt1
- B/PerlReq.pm (grok_import): silence numerical warning

* Wed Nov 21 2007 Alexey Tourbin <at@altlinux.ru> 0.6.6-alt1
- perl.req (isPerl): use plain -T test instead of non-ascii char counter
- perl.{req,prov}.files: use perl's -T test to recheck non-text files

* Sun Sep 30 2007 Alexey Tourbin <at@altlinux.ru> 0.6.5-alt1
- perl.req: implemented support for "perl -x" re-exec hack (fixes cvs2cl.pl)
- perl.req: implemented self-requires elimination for modules outside
  established path, cf. ALT bug #7315

* Thu Sep 06 2007 Alexey Tourbin <at@altlinux.ru> 0.6.4-alt1
- made a few fixes for a special case `use Module 0==0', which is
  internally translated into `Module->import(PL_sv_yes)' and should
  yield `perl(Module) >= 1.0' dependency; this also fixes a regression
  introduced in previous release
- B/PerlReq.pm: in $SIG{__DIE__} handler, resort to Carp::cluck() without
  checking $^S (checking $^S is unreliable since O.pm uses eval)
- resolved some test suite issues (hopefully should pass on perl-5.9.5)

* Fri Aug 17 2007 Alexey Tourbin <at@altlinux.ru> 0.6.3-alt1
- perl.req.files: fixed "text" pattern for file(1)
- B/PerlReq.pm: fixed bug in prevDepF logic
- macros.d/perl5:
  + when doing Build.PL, parse _build/prereqs and dump .perl.req
  + better check for valid Build.PL (must have "dist_name" or "module_name")
- PerlReq/Utils.pm: updated sv_version() algorithm, cf. perlbug 32967
- perl.prov:
  + implemented initial support for version.pm
  + when version assignment is found, check next line if it has
    e.g. '$VERSION = eval $VERSION'
  + strip "use vars" statement before eval, fixes perl-Mozilla-LDAP

* Wed Mar 28 2007 Alexey Tourbin <at@altlinux.ru> 0.6.2-alt1
- B/PerlReq.pm:
  + fixed Carp::confess syntax problem (rt.cpan.org #22512, reported by
    Steve Peters); actually removed Carp::confess and added $^S check
  + added Cygwin pattern to OS-specific dependencies
  + grok_version: do nothing unless version is set, so that the code
    like 'Module->VERSION()', which yields Module version, does not
    produce dependency on the Module
  + enhanced `use encoding ...' and PerlIO dependency detection
- updated test suite for recent perl-5.8 snapshot
- added new files, for possible use with future rpm-build releases:
  + perl.req.files (perl.prov.files) - will select perl files for req/prov
  + /etc/rpm/macros.d/perl.env - piece of rpm-build scriplets' preamble
  + also placed a few rpm-build perl macros to /etc/rpm/macros.d/perl

* Mon Oct 23 2006 Alexey Tourbin <at@altlinux.ru> 0.6.1-alt1
- imported sources into git repo, which is available at
  git://git.altlinux.org/people/at/packages/rpm-build-perl.git
- fixed test suite for recent perl-5.8.x snapshot
- perl.{req,prov}: added pod2usage; removed --debug option, use -vv
- perl.prov: implemented limited support for `$VERSION = $Other::VERSION'

* Wed Jun 07 2006 Alexey Tourbin <at@altlinux.ru> 0.6.0-alt1
- B/PerlReq.pm:
  + major internal cleanup
  + a sketch for event-driven optree analysis blah-blah-blah
  + changed rules for dependencies found in BEGIN blocks:
    - never list ones that have not been loaded according to %%INC,
      except for 'use autouse qw(Module)' case
    - always list loaded ones (there's no easy way to find out if it's been
      loaded by another module; I tried @INC hook + DB::DB debugger trap but
      it didn't work)
  + two-fold speedup
- macros.d/perl5:
  + export PERL_EXTUTILS_AUTOINSTALL=--skip
  + OTHERLDFLAGS="-lperl -lpthread $EXTRA_LIBS" ("full linkage")
- removed %_rpmlibdir/base.pm

* Fri Jun 17 2005 Alexey Tourbin <at@altlinux.ru> 0.5.2-alt2
- B/PerlReq.pm: enhanced PerlIO dependency tracking
- B/Perlreq.pm: dbmopen() requires AnyDBM_File.pm
- macros.d/perl5: export XSUBPP_STATIC_XS=1 -- this will make
  some XS functions static (experimental, perl-5.8.7-alt2)

* Thu Jun 02 2005 Alexey Tourbin <at@altlinux.ru> 0.5.2-alt1
- fixed various perl-5.8.7 build issues
- bumped version and released on CPAN

* Fri Apr 15 2005 Alexey Tourbin <at@altlinux.ru> 0.5.1-alt5
- B/PerlReq.pm: track require_version() calls
- perl.req: restrict LD_LIBRARY_PATH to /usr/lib64 and /usr/lib

* Wed Apr 06 2005 Alexey Tourbin <at@altlinux.ru> 0.5.1-alt4
- B/PerlReq.pm: track PerlIO dependencies for "open" and "binmode"
- perl.prov: allow more opcodes for Safe->reval

* Wed Mar 16 2005 Alexey Tourbin <at@altlinux.ru> 0.5.1-alt3
- %name.spec: use the same %_prefix/lib/rpm directory on x86_64
- perl.prov: decrease verbosity when processing *.al files
- macros.d/perl5: preserve timestamps when making test

* Thu Dec 23 2004 Alexey Tourbin <at@altlinux.ru> 0.5.1-alt2
- perl.req: explode() was not imported

* Wed Dec 22 2004 Alexey Tourbin <at@altlinux.ru> 0.5.1-alt1
- released on CPAN (see %url)
- perl.prov: workaround perl bug #32967
- added partial support for relative paths
- restored OS2 pattern in skip lists (Andrei Bulava, #5713)
- enhanced error handling and debugging output

* Mon Dec 06 2004 Alexey Tourbin <at@altlinux.ru> 0.5-alt1
- bumped version (0.3 -> 0.5) to reflect major changes
- implemented B::PerlReq and made perl.req use it instead of B::Deparse
- new PerlReq::Utils module (convertion and formatting routines)
- version numbers now rounded to 3 digits after decimal point
- v-string versions now treated as floats (e.g. 1.2.3 -> 1.002)
- all dependencies on particular perl version converted to 1:5.x.y form
- enabled version extraction from PREREQ_PM in Makefile.PL
- wrote/updated/enhanced documentation, started README.ALT
- started test suite (more than 50 tests)
- downgraded perl requirements to 5.6.0

* Thu Jul 01 2004 Alexey Tourbin <at@altlinux.ru> 0.3-alt1.1
- perl.req: removed duplicating code
- macros.d/perl: fixed quoting

* Sun Jun 20 2004 Alexey Tourbin <at@altlinux.ru> 0.3-alt1
- macros.d/perl:
  + MDK compatibility: added %%perl_vendor{lib,arch} directories
  + build: fix sharpbang magic lines (with a weired sed expression)
  + MM_install: don't fake PREFIX, rather specify DESTDIR (for gimp-perl)
- perl.req:
  + adjust LD_LIBRARY_PATH for libraries inside buildroot (Yury Konovalov)
  + implemented tracker for dependencies like `use base qw(Foo Bar)'

* Sat May 08 2004 Alexey Tourbin <at@altlinux.ru> 0.2-alt5
- macros.d/perl: added build/install support for Module::Build

* Wed Apr 28 2004 Alexey Tourbin <at@altlinux.ru> 0.2-alt4
- perl.req:
  + s/use v5.8.0/use v5.8.1/ (to stop questions, it's all about B::Deparse)
  + don't simply require perl-base (don't bloat out, it's in basesystem)
- macros.d/perl
  + don't remove comments produced by autosplit (line numbering lost)
  + drop PRINT_PREREQ stuff for a while

* Thu Feb 26 2004 Alexey Tourbin <at@altlinux.ru> 0.2-alt3
- perl.req: try to recover with -M$superclass on failures
- perl.prov: enhanced version detection

* Mon Dec 22 2003 Alexey Tourbin <at@altlinux.ru> 0.2-alt2.2
- yet another hot fix

* Thu Dec 18 2003 Alexey Tourbin <at@altlinux.ru> 0.2-alt2.1
- yet another hot fix

* Thu Dec 18 2003 Alexey Tourbin <at@altlinux.ru> 0.2-alt2
- don't produce dependencies on fake.pm

* Wed Dec 17 2003 Alexey Tourbin <at@altlinux.ru> 0.2-alt1
- fake.pm introduced (@INC entries rearrangement)
- perl.prov manpage introduced
- various fixes

* Tue Nov 04 2003 Alexey Tourbin <at@altlinux.ru> 0.1-alt8
- perl.req:
  + use $RPM_BUILD_ROOT%_bindir/perl whenever available (experimental,
    makes it possible to build incompatible perl)
- macros.d/perl5
  + check for undefined symbols added
  + turned macro arguments into shell function arguments
  + %%CPAN macro added for easy URLs

* Thu Oct 09 2003 Alexey Tourbin <at@altlinux.ru> 0.1-alt7
- perl.req: 
  + counter of perl variables in isPerl() fixed
  + prolog detection enhanced

* Tue Oct 07 2003 Alexey Tourbin <at@altlinux.ru> 0.1-alt6
- perl.req: 
  + isPerl(): try to detect non-perl files (in particular, Polish
    and Prolog *.pl files) and allow failures even in normal mode
  + PRINT_PREREQ dependencies used only in strict mode

* Fri Oct 03 2003 Alexey Tourbin <at@altlinux.ru> 0.1-alt5
- perl.req: strip comments in shebang

* Sun Sep 28 2003 Alexey Tourbin <at@altlinux.ru> 0.1-alt4
- base.pm hacked and placed into %_rpmlibdir in order to avoid
  some weird syntax-check problems

* Fri Sep 26 2003 Alexey Tourbin <at@altlinux.ru> 0.1-alt3
- handling of #!perl command line options implemented

* Tue Sep 23 2003 Alexey Tourbin <at@altlinux.ru> 0.1-alt2
- /etc/rpm/macros.d/perl5 moved here from perl-devel package
- fixed RPM_PERL_LIB_PATH processing

* Thu Sep 18 2003 Alexey Tourbin <at@altlinux.ru> 0.1-alt1
- the package spawned from rpm-build
- fixed handling of taint-mode scripts
- perl.req(1) manual page created

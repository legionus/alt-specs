## SPEC file for Perl module Dist::Zilla::Stash::PodWeaver

%define real_name Dist-Zilla-Stash-PodWeaver

Name: perl-Dist-Zilla-Stash-PodWeaver
Version: 1.005
Release: alt2

Summary: Dist::Zilla plugin to stash of config options for Pod::Weaver

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Dist-Zilla-Stash-PodWeaver/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Thu May 04 2017
# optimized out: perl perl-B-Hooks-EndOfScope perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-Carp-Clan perl-Class-Data-Inheritable perl-Class-Load perl-Class-Singleton perl-Clone perl-Config-INI perl-Config-MVP perl-Config-MVP-Reader-INI perl-Config-MVP-Slicer perl-Data-OptList perl-Data-Section perl-DateTime perl-DateTime-Locale perl-DateTime-TimeZone perl-Devel-GlobalDestruction perl-Devel-OverloadInfo perl-Devel-StackTrace perl-Dist-Zilla perl-Encode perl-Eval-Closure perl-Exception-Class perl-Exporter-Tiny perl-File-Copy-Recursive perl-File-Find-Rule perl-File-pushd perl-IO-String perl-IPC-Run3 perl-List-MoreUtils perl-Log-Dispatch perl-Log-Dispatch-Array perl-Log-Dispatchouli perl-MRO-Compat perl-Mixin-Linewise perl-Module-Implementation perl-Module-Pluggable perl-Module-Runtime perl-Moo perl-Moose perl-MooseX-LazyRequire perl-MooseX-OneArgNew perl-MooseX-Role-Parameterized perl-MooseX-SetOnce perl-MooseX-Types perl-MooseX-Types-Perl perl-Number-Compare perl-PPI perl-Package-DeprecationManager perl-Package-Stash perl-Package-Stash-XS perl-Params-Util perl-Params-Validate perl-Params-ValidationCompiler perl-Parse-CPAN-Meta perl-Path-Tiny perl-PerlIO-utf8_strict perl-Pod-Eventual perl-Probe-Perl perl-Role-HasMessage perl-Role-Identifiable perl-Role-Tiny perl-Software-License perl-Specio perl-String-Flogger perl-String-RewritePrefix perl-Sub-Exporter perl-Sub-Exporter-ForMethods perl-Sub-Exporter-Progressive perl-Sub-Identify perl-Sub-Install perl-Sub-Name perl-Sub-Quote perl-Text-Glob perl-Text-Template perl-Throwable perl-Tie-IxHash perl-Tie-RefHash perl-Try-Tiny perl-Variable-Magic perl-YAML-Tiny perl-aliased perl-autodie perl-devel perl-namespace-autoclean perl-namespace-clean perl-parent perl-unicore python-base python-modules python3
BuildRequires: perl-Class-XSAccessor perl-Dist-Zilla-Role-DynamicConfig perl-Dist-Zilla-Role-Stash-Plugins perl-PPI-XS perl-Pod-Weaver perl-Ref-Util perl-Test-MockObject perl-Test-Script

%description
Perl module Dist::Zilla::Stash::PodWeaver provides is intended
to allow to set other options in dist.ini that can be accessed
by Pod::Weaver plugins.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Dist/Zilla/Stash/PodWeaver*

%changelog
* Thu May 04 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.005-alt2
- Initial build for ALT Linux Sisyphus

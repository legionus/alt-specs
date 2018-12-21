%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN.pm) perl(Carp.pm) perl(Config.pm) perl(Cwd.pm) perl(Data/Dumper.pm) perl(Exporter.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Path.pm) perl(File/Slurp.pm) perl(FileHandle.pm) perl(Filter/Util/Call.pm) perl(LWP/Simple.pm) perl(MIME/Base64.pm) perl(Module/Build.pm) perl(PerlIO.pm) perl(Pod/Html.pm) perl(Pod/Man.pm) perl(Pod/Text.pm) perl(Test/Deep.pm) perl(YAML.pm) perl(YAML/Tiny.pm) perl(overload.pm) perl(threads/shared.pm)
# END SourceDeps(oneline)
%define module_name Test-Time
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.07
Release: alt1
Summary: Overrides the time() and sleep() core functions for testing
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/S/SA/SATOH/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
Test::Time can be used to test modules that deal with time. Once you `use' this 
module, all references to `time' and `sleep' will be internalized. You can set
custom time by passing time => number after the `use' statement:

    use Test::Time time => 1;

    my $now = time;    # $now is equal to 1
    sleep 300;         # returns immediately, displaying a note
    my $then = time;   # $then equals to 301


%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes README.md
%perl_vendor_privlib/T*

%changelog
* Mon Oct 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Thu Jun 28 2018 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Wed Aug 30 2017 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- moved to Sisyphus as dependency

* Tue Sep 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- initial import by package builder


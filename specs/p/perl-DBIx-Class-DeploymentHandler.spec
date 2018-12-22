%define _unpackaged_files_terminate_build 1
%define sname dbix-class-deploymenthandler

Name:           perl-DBIx-Class-DeploymentHandler
Version:        0.002222
Release:        alt1
Summary:        Extensible DBIx::Class deployment
License:        GPL-1.0-or-later or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/DBIx-Class-DeploymentHandler/
Source:         %sname-%version.tar
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-Package-Generator
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Carp/Clan.pm)
BuildRequires:  perl(Context/Preserve.pm)
BuildRequires:  perl(DBD/SQLite.pm)
BuildRequires:  perl(DBI.pm)
BuildRequires:  perl(DBIx/Class/Core.pm)
BuildRequires:  perl(DBIx/Class/ResultSet.pm)
BuildRequires:  perl(DBIx/Class/Schema.pm)
BuildRequires:  perl(DBIx/Class/Schema/Loader.pm)
BuildRequires:  perl(DBIx/Class/Storage.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Log/Contextual.pm)
BuildRequires:  perl(Log/Contextual/Role/Router.pm)
BuildRequires:  perl(Log/Contextual/WarnLogger.pm)
BuildRequires:  perl(Module/Runtime.pm)
BuildRequires:  perl(Moo.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(Moose/Role.pm)
BuildRequires:  perl(Moose/Util.pm)
BuildRequires:  perl(Moose/Util/TypeConstraints.pm)
BuildRequires:  perl(MooseX/Role/Parameterized.pm)
BuildRequires:  perl(Path/Class.pm)
BuildRequires:  perl(SQL/Translator.pm)
BuildRequires:  perl(SQL/Translator/Diff.pm)
BuildRequires:  perl(Sub/Exporter/Progressive.pm)
BuildRequires:  perl(Test/Fatal.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Requires.pm)
BuildRequires:  perl(Text/Brew.pm)
BuildRequires:  perl(Time/HiRes.pm)
BuildRequires:  perl(Try/Tiny.pm)
BuildRequires:  perl(aliased.pm)
BuildRequires:  perl(autodie.pm)
BuildRequires:  perl(base.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(namespace/autoclean.pm)
BuildRequires:  perl(parent.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)

%description
DBIx::Class::DeploymentHandler is, as its name suggests, a tool for deploying
and upgrading databases with DBIx::Class. It is designed to be much more
flexible than DBIx::Class::Schema::Versioned, hence the use of Moose and lots
of roles.

%prep
%setup -q -n %sname-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes TODO
%{perl_vendorlib}/DBIx/Class/DeploymentHandler*

%changelog
* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 0.002222-alt1
- initial build for ALT

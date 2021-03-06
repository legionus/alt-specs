%define _unpackaged_files_terminate_build 1
BuildRequires: perl(Module/Build.pm)
#
#   - TheSchwartz -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       TheSchwartz
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module TheSchwartz
%define m_distro TheSchwartz
%define m_name TheSchwartz
%define m_author_id unknown
%define _enable_test 1

Name: perl-TheSchwartz
Version: 1.12
Release: alt2

Summary: TheSchwartz is a reliable job queue system

License: Artistic
Group: Development/Perl
Url: %CPAN %m_distro

Packager: Denis Baranov <baraka@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/J/JF/JFEARN/TheSchwartz-%{version}.tar.gz

# Automatically added by buildreq on Fri Jun 21 2013
BuildRequires: perl-Data-ObjectDriver perl-devel

%description
TheSchwartz is a reliable job queue system.
Your application can put jobs into the system, and your worker processes 
can pull jobs from the queue atomically to perform. Failed jobs can be 
left in the queue to retry later.

Abilities specify what jobs a worker process can perform.
Abilities are the names of TheSchwartz::Worker subclasses, 
as in the synopsis: the MyWorker class name is used to specify 
that the worker script can perform the job. When using 
the TheSchwartz client's work functions, the class-ability duality 
is used to automatically dispatch to the proper class to do the actual work.

%prep
%setup -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/schwartzmon
%_man1dir/schwartzmon*
%perl_vendor_privlib/TheSchwartz.pm
%perl_vendor_privlib/TheSchwartz/

%changelog
* Fri Jun 29 2018 Igor Vlasenko <viy@altlinux.ru> 1.12-alt2
- fixed unpackaged files

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1
- automated CPAN update

* Fri Jun 21 2013 Vitaly Lipatov <lav@altlinux.ru> 1.10-alt2
- cleanup spec, fix packing

* Thu Mar 10 2011 Denis Baranov <baraka@altlinux.ru> 1.10-alt1
- initial build for ALT Linux Sisyphus


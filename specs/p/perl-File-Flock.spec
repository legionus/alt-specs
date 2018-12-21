%define _unpackaged_files_terminate_build 1
#
#   - File::Flock -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --spec-only File::Flock
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module File-Flock
%define m_distro File-Flock
%define m_name File::Flock
%define m_author_id unknown
%define _enable_test 1

Name: perl-File-Flock
Version: 2014.01
Release: alt1

Summary: Wrapper for flock() to make file locking trivial

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Denis Baranov <baraka@altlinux.org>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/M/MU/MUIR/modules/File-Flock-%{version}.tar.gz

# Automatically added by buildreq on Tue Nov 30 2010
BuildRequires: libnss-role perl-devel perl(Module/Build.pm) perl(Data/Structure/Util.pm) perl(File/Slurp.pm) perl(IO/Event.pm) perl(Test/SharedFork.pm)

%description
Lock files using the flock() call.  If the file to be locked does not
exist, then the file is created.  If the file was created then it will
be removed when it is unlocked assuming it's still an empty file.

Locks can be created by new'ing a File::Flock object.  Such locks
are automatically removed when the object goes out of scope.  The
unlock() method may also be used.

lock_rename() is used to tell File::Flock when a file has been
renamed (and thus the internal locking data that is stored based
on the filename should be moved to a new name).  unlock() the
new name rather than the original name.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/File/*

%changelog
* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 2014.01-alt1
- automated CPAN update

* Wed Oct 09 2013 Igor Vlasenko <viy@altlinux.ru> 2013.11-alt1
- automated CPAN update

* Tue Nov 30 2010 Denis Baranov <baraka@altlinux.org> 2008.01-alt1
- initial build for ALT Linux Sisyphus

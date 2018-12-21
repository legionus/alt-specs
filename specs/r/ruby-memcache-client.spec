%define pkgname memcache-client

Name: ruby-%pkgname
Version: 1.7.4
Release: alt1.3
Summary: Ruby client for Danga Interactive's memcached
License: MIT
Group: Development/Ruby
Url: http://rubyforge.org/projects/seattlerb/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

BuildArch: noarch

# Automatically added by buildreq on Tue Jul 08 2008 (-bi)
BuildRequires: rpm-build-ruby ruby-flexmock ruby-tool-rdoc ruby-tool-setup
BuildRequires: ruby-test-unit

%description
memcache-client is a client for Danga Interactive's memcached.

%package doc
Summary: Documentation files for %pkgname
Group: Documentation

%description doc
Documentation files for %pkgname

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb
# Useless crap.
rm -f lib/continuum_native.rb

%build
%ruby_config
%ruby_build
#%%ruby_test_unit -Ilib test/

%install
%ruby_install
%rdoc lib/

%files
%doc History.rdoc README.rdoc
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/MemCache*

%changelog
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.4-alt1.3
- Rebuild with new Ruby autorequirements.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.7.4-alt1.2
- Rebuild with Ruby 2.4.1

* Sat Dec 08 2012 Led <led@altlinux.ru> 1.7.4-alt1.1
- Rebuilt with ruby-1.9.3-alt1
- fixed BuildRequires

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 1.7.4-alt1
- [1.7.4]

* Tue Jul 08 2008 Sir Raorn <raorn@altlinux.ru> 1.5.0-alt1
- Built for Sisyphus


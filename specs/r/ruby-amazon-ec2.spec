%define  pkgname amazon-ec2

Name: 	 ruby-%pkgname
Version: 0.9.17 
Release: alt2.1

Summary: A Ruby Gem that gives you full access to several of the Amazon Web Services API from your Ruby/Ruby on Rails apps
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/grempe/amazon-ec2

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
# For tests
BuildRequires: ruby-test-spec
BuildRequires: ruby-mocha
BuildRequires: ruby-xml-simple

%description
%summary

%package doc
Summary: Documentation files for %name
Group: Documentation

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
rm -rf %buildroot%_bindir/setup.rb
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
#%%ruby_test_unit -Ilib:test test

%files
%doc README*
%_bindir/awshell
%_bindir/ec2*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.17-alt2.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Fri Jun 08 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.17-alt2
- Fix tests.

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.17-alt1
- Initial build for Sisyphus.

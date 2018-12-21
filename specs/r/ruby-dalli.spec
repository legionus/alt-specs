%define  pkgname dalli

%filter_from_requires /^ruby(inline)/d
%filter_from_requires /^ruby(action_dispatch\/middleware\/session\/abstract_store)/d

Name: ruby-%pkgname
Version: 2.7.6
Release: alt1.2

Summary: High performance memcached client for Ruby
License: MIT
Group:   Development/Ruby
Url:     https://github.com/petergoldstein/dalli
BuildArch: noarch
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
Source:  %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel
BuildRequires: memcached

%description
High performance memcached client for Ruby.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
#%%ruby_test_unit -Ilib:test test

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/*

%changelog
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.7.6-alt1.2
- Rebuild with new Ruby autorequirements.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.7.6-alt1.1
- Rebuild with Ruby 2.4.1

* Thu Aug 31 2017 Alexey Shabalin <shaba@altlinux.ru> 2.7.6-alt1
- Initial build in Sisyphus


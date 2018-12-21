%define  pkgname mixlib-cli
 
Name: 	 ruby-%pkgname
Version: 1.7.6
Release: alt1
 
Summary: A mixin for creating command line applications
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/chef/mixlib-cli
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
Mixlib::CLI provides a class-based command line option parsing object,
like the one used in Chef, Ohai and Relish.

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
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}
 
%check
%ruby_test_unit -Ilib:test test
 
%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.6-alt1
- New version.

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.5-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.5.0-alt1
- Initial build for ALT Linux

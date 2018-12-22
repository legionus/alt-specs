%define  pkgname thor
 
Name: 	 ruby-%pkgname
Version: 0.19.1 
Release: alt1.1
 
Summary: Thor is a toolkit for building powerful command-line interfaces.
License: MIT or Ruby
Group:   Development/Ruby
Url:     http://whatisthor.com/
# VCS:	 https://github.com/erikhuda/thor

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
Thor is a simple and efficient tool for building self-documenting
command line utilities. It removes the pain of parsing command line
options, writing "USAGE:" banners, and can also be used as an
alternative to the Rake build tool. The syntax is Rake-like, so it
should be familiar to most Rake users.

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
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.19.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri May 22 2015 Andrey Cherepanov <cas@altlinux.org> 0.19.1-alt1
- Initial build for ALT Linux

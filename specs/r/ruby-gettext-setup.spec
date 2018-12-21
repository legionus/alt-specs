%define  pkgname gettext-setup
 
Name: 	 ruby-%pkgname
Version: 0.30
Release: alt2
 
Summary: A gem that configures gettext for internationalization
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/puppetlabs/gettext-setup-gem
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
Patch1: update-fast-gettext-to-1.7.patch
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

Requires: ruby-gettext
Requires: ruby-locale
 
%description
This is a simple gem to set up i18n for Ruby projects (including Sinatra
web apps) using gettext and fast gettext.

This project sets the default locale to English. If the user has set a
different locale in their browser preferences, and we support the user's
preferred locale, strings and data formatting will be customized for
that locale.

%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%patch1 -p 1
# Adapt gemspec for package
subst 's,\(spec.version.*=\).*,\1 %version,' %pkgname.gemspec
subst 's,\(spec.files.*=\).*,\1 Dir["%ruby_sitelibdir/%pkgname*"],' %pkgname.gemspec
subst '/spec.test_files/d' %pkgname.gemspec

# Fix path
subst 's,metadata_pot/,gettext-setup/,' lib/generate_metadata_pot.rb
%update_setup_rb
# Fix missing trailing new line symbol
echo >> lib/gettext-setup.rb
 
%build
%ruby_config
%ruby_build
 
%install
%ruby_install
# Install gemspec
export rbVersion=`ruby -e "puts RbConfig::CONFIG[\"ruby_version\"]"`
install -Dm 0644 %pkgname.gemspec %buildroot%ruby_libdir/gems/$rbVersion/specifications/%pkgname.gemspec

%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}
 
%check
%ruby_test_unit -Ilib:test test
 
%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*
%ruby_libdir/gems/*/specifications/*.gemspec

%files doc
%ruby_ri_sitedir/*
 
%changelog
* Tue Sep 25 2018 Pavel Skrylev <majioa@altlinux.org> 0.30-alt2
- Update fastgettext to 1.7

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.30-alt1.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.30-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.30-alt1.1
- Rebuild with Ruby 2.5.0

* Tue Feb 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.30-alt1
- New version.

* Sat Dec 02 2017 Andrey Cherepanov <cas@altlinux.org> 0.29-alt1
- New version.

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 0.28-alt2
- Rebuild with Ruby 2.4.2

* Sat Sep 02 2017 Andrey Cherepanov <cas@altlinux.org> 0.28-alt1
- New version

* Wed Jul 12 2017 Andrey Cherepanov <cas@altlinux.org> 0.26-alt1
- New version

* Wed May 31 2017 Andrey Cherepanov <cas@altlinux.org> 0.25-alt1
- New version

* Fri Apr 21 2017 Andrey Cherepanov <cas@altlinux.org> 0.24-alt1
- New version
- Package gemspec
- Require dependencies from gemspec

* Thu Mar 30 2017 Andrey Cherepanov <cas@altlinux.org> 0.20-alt1
- New version

* Mon Mar 20 2017 Andrey Cherepanov <cas@altlinux.org> 0.16-alt1
- New version

* Tue Feb 28 2017 Andrey Cherepanov <cas@altlinux.org> 0.13-alt1
- New version

* Mon Oct 24 2016 Andrey Cherepanov <cas@altlinux.org> 0.7-alt1
- Initial build in Sisyphus

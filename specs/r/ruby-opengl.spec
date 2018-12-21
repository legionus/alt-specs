Name:    ruby-opengl
Version: 0.9.2
Release: alt2.5
Epoch:   1
Summary: OpenGL Interface for Ruby
License: MIT
Group: Development/Ruby
Url: https://github.com/larskanis/opengl
Source: ruby-opengl-%{version}.tar

BuildRequires: libGL-devel libX11-devel libfreeglut-devel libruby-devel
BuildRequires: ruby-tool-setup
BuildRequires: ruby-hoe rake-compiler

%filter_from_requires /^ruby(glu/d
%description
ruby-opengl consists of Ruby extension modules that are bindings for
the OpenGL, GLU, and GLUT libraries. It is intended to be a replacement
for -- and uses the code from -- Yoshi's ruby-opengl.

%prep
%setup
%update_setup_rb
 
%build
%ruby_config
%ruby_build
rake debug_gem > opengl.gemspec
 
%install
%ruby_install

%files
%ruby_sitelibdir/*
%rubygem_specdir/*
%ruby_sitearchdir/*

%changelog
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.9.2-alt2.5
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.9.2-alt2.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1:0.9.2-alt2.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.2-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.2-alt2.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 1:0.9.2-alt2
- Rebuild with new %%ruby_sitearchdir location

* Tue Sep 27 2016 Andrey Cherepanov <cas@altlinux.org> 1:0.9.2-alt1
- New version from new homepage

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.60.1-alt2.2
- Rebuilt with ruby-2.0.0-alt1

* Sun Dec 09 2012 Led <led@altlinux.ru> 0.60.1-alt2.1
- Rebuilt with ruby-1.9.3-alt1
- fixed BuildRequires

* Sun Sep 26 2010 Alexey I. Froloff <raorn@altlinux.org> 0.60.1-alt2
- Rebuild with Ruby 1.9.2

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 0.60.1-alt1
- [0.60.1]

* Thu Apr 03 2008 Sir Raorn <raorn@altlinux.ru> 0.60-alt1
- Rebuilt with rpm-build-ruby
- Based on unpublished build:
  * Mon Mar 24 2008 Kirill A. Shutemov <kas@altlinux.ru> 0.60-alt1
  - 0.60
  - new upstream maintainer(see http://ruby-opengl.rubyforge.org/)
  - MIT licence

* Sat May 08 2004 Kirill A. Shutemov <kas@altlinux.ru> 0.32d-alt4
- New version
- Use default gcc for building

* Fri Feb 13 2004 Kirill A. Shutemov <kas@altlinux.ru> 0.32b-alt3
- BuildRequires fixed

* Thu Feb 05 2004 Kirill A. Shutemov <kas@altlinux.ru> 0.32b-alt2
- Use set_gcc_version to select gcc

* Sat Jan 10 2004 Kirill A. Shutemov <kas@altlinux.ru> 0.32b-alt1
- First Build for ALT project

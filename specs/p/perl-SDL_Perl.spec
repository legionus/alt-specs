%filter_from_provides /^perl\\\(SDL\\\.pm\\\)/d
%define dist SDL_Perl
Name: perl-%dist
Version: 2.2.6
Release: alt10.1.1

Summary: Simple DirectMedia Layer for Perl
License: LGPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-v%version.tar.gz
Patch: SDL_Perl-v2.2.6-alt-perl522-syntax.patch
# https://bugzilla.altlinux.org/show_bug.cgi?id=30568
Patch1: fix_modify_readonly_value.patch

Provides: perl-SDL = %version
Obsoletes: perl-SDL < 2.2.6-alt9
Conflicts: perl-SDL < 2.2.6-alt9

# avoid crazy dependencies
%add_findreq_skiplist */SDL/Tutorial*

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: libSDL_gfx-devel libSDL_image-devel libSDL_mixer-devel libSDL_net-devel libSDL_ttf-devel libjpeg-devel libpng-devel libsmpeg-devel perl-Module-Build

%package -n perl-SDL-OpenGL
Summary: Simple DirectMedia Layer for Perl (OpenGL)
Group: Development/Perl
Requires: %name = %version-%release
Provides: perl-SDL_Perl-OpenGL = %version

%description
SDL_Perl is a wrapper around the cross platform Simple DirectMedia Layer
game library. Essentially it allows to write cross platform games in Perl,
using 2d (SDL), or 3d (OpenGL), or a combination of both if you wish.

%description -n perl-SDL-OpenGL
SDL_Perl is a wrapper around the cross platform Simple DirectMedia Layer
game library. Essentially it allows to write cross platform games in Perl,
using 2d (SDL), or 3d (OpenGL), or a combination of both if you wish.

%prep
%setup -q -n %dist-v%version
%patch -p1
%patch1 -p0

# avoid build dependency on YAML
sed -i- '/^use YAML/d' Build.PL

%ifdef __BTE
# mixer is not available in restricted environment
mv t/mixerpm.t t/mixerpm.t.orig
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

# Check that our Module::Build links perl extensions with -lperl.
objdump -p %buildroot%perl_vendor_autolib/SDL_perl/SDL_perl.so |egrep 'NEEDED[[:space:]]+libperl'

%files
%doc BUGS CHANGELOG README TODO
%perl_vendor_archlib/SDL*
%perl_vendor_autolib/SDL*
%exclude %perl_vendor_archlib/SDL/OpenGL*
%exclude %perl_vendor_autolib/SDL/OpenGL*

%files -n perl-SDL-OpenGL
%perl_vendor_archlib/SDL/OpenGL*
%perl_vendor_autolib/SDL/OpenGL*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt10.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt10.1
- rebuild with new perl 5.24.1

* Wed Jun 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt10
- added Provides: perl-SDL = version to help upgrade (closes: #32191)

* Tue Jun 14 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt9
- renamed: perl-SDL -> perl-SDL_Perl

* Tue Jun 14 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt8
- prepared to be renamed as perl-SDL_Perl

* Sun Jan 17 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt7
- added patch from ALT#30568

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt6.1
- rebuild with new perl 5.22.0

* Fri Nov 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt6
- syntax fixes for perl 5.22

* Thu Nov 19 2015 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt5.1.1
- rebuild with new perl 5.20.1

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt5.1
- rebuild with new perl 5.20.1

* Thu Dec 04 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt5
- rebuild with new SDL

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 2.2.6-alt4
- built for perl 5.18

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 2.2.6-alt3
- rebuilt for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 2.2.6-alt2.2
- rebuilt for perl-5.14
- rebuilt as plain src.rpm

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 2.2.6-alt2.1
- rebuilt with perl 5.12
- fixed build

* Sun Apr 04 2010 Alexey Tourbin <at@altlinux.ru> 2.2.6-alt2
- Build.PL: eliminated build dependency on YAML

* Wed Feb 17 2010 Alexey Tourbin <at@altlinux.ru> 2.2.6-alt1
- 2.1.3 -> 2.2.6

* Sun Oct 28 2007 Alexey Tourbin <at@altlinux.ru> 2.1.3-alt3
- applied debian/patches/030_opengl_fixes.diff

* Tue Aug 14 2007 Alexey Tourbin <at@altlinux.ru> 2.1.3-alt2
- fixed building with new Module::Build

* Fri Oct 21 2005 Alexey Tourbin <at@altlinux.ru> 2.1.3-alt1
- 2.1.2 -> 2.1.3
- alt-sdl_link.patch merged upstream (cpan #11383)

* Fri Feb 04 2005 Alexey Tourbin <at@altlinux.ru> 2.1.2-alt1
- 1.20.0 -> 2.1.2, major revision
- new subpackage: %name-OpenGL
- alt-sdl_link.patch: fixed linkage (cpan #11383)
- built against new SDL_gfx
- manual pages not packaged (use perldoc)
- updated URL

* Fri Jun 20 2003 Sergey V Turchin <zerg at altlinux dot org> 1.20.0-alt1.1
- rebuild with new SDL_gfx

* Tue Mar 18 2003 Stanislav Ievlev <inger@altlinux.ru> 1.20.0-alt1
- 1.20.0

* Thu Oct 31 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.19.0-alt1
- 1.19.0
- Rebuilt with new perl

* Fri Jun 07 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.18-alt1
- 1.18

* Mon May 27 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.18-1mdk
- new stable release

* Sat May 11 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.16-3mdk
- s/SDL::Error/SDL::GetError/ in one pm

* Mon Apr 29 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.16-2mdk
- fix url
- rebuild for new alsa
- fix buildrequires

* Mon Apr 15 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.16-1mdk
- new version
  - patching Makefile.PL no more needed

* Mon Apr  8 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.11-3mdk
- my mistake, it's LGPL, not GPL

* Tue Mar  5 2002 Grigory Milev <week@altlinux.ru> 1.11-alt1
- ALTLinux adaptation

* Fri Feb 22 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.11-2mdk
- add dependency on perl

* Mon Jan 28 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.11-1mdk
- new version with another patch sent to author integrated right away

* Wed Jan 23 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.10-1mdk
- new release from author
- my SDL::Music patch integrated upstream

* Tue Jan 22 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.08-6mdk
- patch SDL::Music.pm where DESTROY was not calling the right function
  (who's using this library apart me anyway? ;p)

* Mon Oct 15 2001 Stefan van der Eijk <stefan@eijk.nu> 1.08-5mdk
- BuildRequires: libjpeg-devel perl-devel

* Fri Oct 12 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.08-4mdk
- rebuild for libpng3
- fix URL

* Thu Jul  5 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.08-3mdk
- rebuild

* Mon May 14 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.08-2mdk
- new SDL

* Tue Jan  2 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.08-1mdk
- first package in Linux-Mandrake

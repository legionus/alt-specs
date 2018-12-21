Name: common-licenses
Version: 1.4
Release: alt1

Summary: Contains the various common licenses used in the %distribution
License: distributable
Group: System/Base
BuildArch: noarch
Packager: Dmitry V. Levin <ldv@altlinux.org>
Prefix: %prefix

Source: license.tar

%description
Contains the various common licenses uses by the %distribution.
Instead of including the COPYING file in every package,
just refer to this one.

%prep
%setup -q -n license

%install
mkdir -p %buildroot%_licensedir  %buildroot%_licensedir-exception
cp -dp license/* %buildroot%_licensedir
cp -dp exception/* %buildroot%_licensedir-exception

%files
%_licensedir
%_licensedir-exception

%changelog
* Fri Nov 09 2018 Alexey Gladkov <legion@altlinux.ru> 1.4-alt1
- Add licenses from SPDX version 3.3 2018-10-24 (https://spdx.org/licenses/).
- Add licenses exceptions from SPDX version 3.2 (https://spdx.org/licenses/exceptions-index.html).
- Add aliases without version for licenses without variants.

* Thu Sep 20 2007 Dmitry V. Levin <ldv@altlinux.org> 1.3-alt1
- Adeed new licenses:
  + FDL-1.2, GPL-3, LGPL-3: Imported from ftp://ftp.gnu.org/gnu/Licenses/ (#12612)
  + Artistic-2: Imported from http://www.perlfoundation.org/attachment/legal/artistic-2_0.txt
  + ISC: Imported from dhcp-3.0.6

* Fri Jul 01 2005 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt1
- Updated: FDL-1.1, GPL-2, LGPL-2.1.
  (updated FSF postal mail address).

* Mon Aug 09 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2-alt1
- Updated: GPL-2, LGPL-2.0, LGPL-2.1.
- Added: GPL-1, Apache-2.0, ZPL-2.1.

* Thu Jun 21 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.1-alt1
- Changed license of this package to "distributable".

* Tue Jan 30 2001 Dmitry V. Levin <ldv@fandra.org> 1.0-ipl1mdk
- Initial revision.

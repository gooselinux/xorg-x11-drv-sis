%define tarball xf86-video-sis
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

Summary:   Xorg X11 sis video driver
Name:      xorg-x11-drv-sis
Version:   0.10.2
Release:   1.1%{?dist}
URL:       http://www.x.org
License:   MIT
Group:     User Interface/X Hardware Support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2
Source1:   sis.xinf

ExcludeArch: s390 s390x

BuildRequires: xorg-x11-server-sdk >= 1.4.99.1
BuildRequires: mesa-libGL-devel >= 6.4-4
BuildRequires: libdrm-devel >= 2.0-1

Requires:  hwdata
Requires:  xorg-x11-server-Xorg >= 1.4.99.1

%description 
X.Org X11 sis video driver.

%prep
%setup -q -n %{tarball}-%{version}

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases/

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/sis_drv.so
%{_datadir}/hwdata/videoaliases/sis.xinf
%{_mandir}/man4/sis.4*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.10.2-1.1
- Rebuilt for RHEL 6

* Tue Aug 04 2009 Dave Airlie <airlied@redhat.com> 0.10.2-1
- sis 0.10.2

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 0.10.1-3.1
- ABI bump

* Tue Jun 23 2009 Dave Airlie <airlied@redhat.com> 0.10.1-3
- abi.patch: fixup for new server ABI

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Dave Airlie <airlied@redhat.com> 0.10.1-1
- Latest upstream release

* Thu Mar 20 2008 Dave Airlie <airlied@redhat.com> 0.10.0-1
- Latest upstream release

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.4-4
- Autorebuild for GCC 4.3

* Thu Jan 17 2008 Dave Airlie <airlied@redhat.com> - 0.9.4-3
- fix more bugs in pciaccess port - tested on actual hardware.

* Wed Jan 16 2008 Dave Airlie <airlied@redhat.com> - 0.9.4-2
- fixup bugs in pciaccess port

* Wed Jan 16 2008 Dave Airlie <airlied@redhat.com> - 0.9.4-1
- new upstream version
- sis-pciaccess.patch - add initial pciaccess port

* Wed Aug 22 2007 Adam Jackson <ajax@redhat.com> - 0.9.3-4
- Rebuild for PPC toolchain bug

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 0.9.3-3
- Update Requires and BuildRequires.  Disown the module directories.  Add
  Requires: hwdata.

* Fri Feb 16 2007 Adam Jackson <ajax@redhat.com> 0.9.3-2
- ExclusiveArch -> ExcludeArch

* Fri Dec 1 2006 Adam Jackson <ajax@redhat.com> 0.9.3-1
- Update to 0.9.3

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 0.9.1-7
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Wed Sep 20 2006 Adam Jackson <ajackson@redhat.com> 0.9.1-6
- sis-0.9.1-assert.patch: Include assert.h so we don't crash.

* Thu Aug 17 2006 Bill Nottingham <notting@redhat.com> 0.9.1-5
- fix sis.xinf for XGI (case sensitive)

* Mon Jul 24 2006 Adam Jackson <ajackson@redhat.com> 0.9.1-4
- Update sis.xinf for XGI cards.  (#186024)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 0.9.1-3.1
- rebuild

* Fri May 26 2006 Mike A. Harris <mharris@redhat.com> 0.9.1-3
- Added "BuildRequires: libdrm-devel >= 2.0-1" for (#192358)
- Bumped sdk dep to pick up proto-devel indirectly.

* Tue May 23 2006 Adam Jackson <ajackson@redhat.com> 0.9.1-2
- Rebuild for 7.1 ABI fix.

* Sun Apr  9 2006 Adam Jackson <ajackson@redhat.com> 0.9.1-1
- Update to 0.9.1 from 7.1RC1.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.8.1.3-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.8.1.3-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 0.8.1.3-1
- Updated xorg-x11-drv-sis to version 0.8.1.3 from X11R7.0

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 0.8.1.2-1
- Updated xorg-x11-drv-sis to version 0.8.1.2 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 0.8.1-1
- Updated xorg-x11-drv-sis to version 0.8.1 from X11R7 RC2
- Added "BuildRequires: mesa-libGL-devel >= 6.4-4" for DRI-enabled builds.

* Fri Nov 4 2005 Mike A. Harris <mharris@redhat.com> 0.8.0.1-1
- Updated xorg-x11-drv-sis to version 0.8.0.1 from X11R7 RC1
- Fix *.la file removal.

* Tue Oct 4 2005 Mike A. Harris <mharris@redhat.com> 0.7.0-1
- Update BuildRoot to use Fedora Packaging Guidelines.
- Deglob file manifest.
- Limit "ExclusiveArch" to x86, x86_64, ppc

* Fri Sep 2 2005 Mike A. Harris <mharris@redhat.com> 0.7.0-0
- Initial spec file for sis video driver generated automatically
  by my xorg-driverspecgen script.

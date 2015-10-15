%define pre	rc5

%define distname	%{name}-%{version}-%{pre}.tar.bz2
%define dname		%{name}-%{version}~%{pre}

%define major		2
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary:	Font rendering library for OpenGL applications
Name:		ftgl
Version:	2.1.3
Release:	0.%{pre}.9
License:	MIT
Group:		System/Libraries
URL:		http://ftgl.wiki.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{distname}
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(glu)

%description
FTGL is a free, open source library to enable developers to use arbitrary
fonts in their OpenGL (www.opengl.org) applications.  Unlike other OpenGL
font libraries FTGL uses standard font file formats so doesn't need a
preprocessing step to convert the high quality font data into a lesser
quality, proprietary format.  FTGL uses the Freetype (www.freetype.org)
font library to open and 'decode' the fonts. It then takes that output
and stores it in a format most efficient for OpenGL rendering.

Rendering modes supported are:
     * Bit maps
     * Anti aliased pix maps
     * Texture maps
     * Outlines
     * Polygon meshes
     * Extruded polygon meshes

%package -n	%{libname}
Summary:	OpenGL Interface of Freetype2
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Provides:	%{libname} = %{version}-%{release}

%description -n	%{libname}
FTGL is a free, open source library to enable developers to use arbitrary
fonts in their OpenGL (www.opengl.org) applications.  Unlike other OpenGL
font libraries FTGL uses standard font file formats so doesn't need a
preprocessing step to convert the high quality font data into a lesser
quality, proprietary format.  FTGL uses the Freetype (www.freetype.org)
font library to open and 'decode' the fonts. It then takes that output
and stores it in a format most efficient for OpenGL rendering.

Rendering modes supported are:
     * Bit maps
     * Anti aliased pix maps
     * Texture maps
     * Outlines
     * Polygon meshes
     * Extruded polygon meshes

%package -n	%{develname}
Summary:	Development related files of FTGL
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{develname}
This package contains headers and static libraries of FTGL.
You need to install it if you want to develop or compile
any programs that make use of OpenGL interface of freetype
library.

%prep
%setup -q -n %{dname}
find -type f -name '*.txt' -print0 | xargs -0 -r %__chmod 0644

%build
export LIBS=-lm

%configure2_5x --enable-shared --disable-static
%make

%install
%makeinstall

# include doc ourselves, don't let software do it
%__rm -rf %{buildroot}%{_docdir}

# remove files not bundled
%__rm -f %{buildroot}%{_bindir}/FTGLDemo
%__rmdir %{buildroot}%{_bindir} || true


%files -n %{libname}
%{_libdir}/libftgl.so.%{major}*

%files -n %{develname}
%doc AUTHORS BUGS NEWS README TODO
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Apr 10 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2.1.3-0.rc5.8mdv2011.0
- Don't use %%dirname macro which seems to be reserved in RPM5

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1.3-0.rc5.5mdv2011.0
+ Revision: 664394
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.3-0.rc5.4mdv2011.0
+ Revision: 605218
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.3-0.rc5.3mdv2010.1
+ Revision: 522675
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.1.3-0.rc5.2mdv2010.0
+ Revision: 424483
- rebuild

* Tue Dec 09 2008 Adam Williamson <awilliamson@mandriva.org> 2.1.3-0.rc5.1mdv2009.1
+ Revision: 312109
- new major 2
- fix doc file list
- no more unix/ subdir for build, no need to re-gen build scripts any more
- drop all patches (no longer needed)
- correct license
- update URLs
- bump to 2.1.3rc5 (for chromium, and fixes a bunch of stuff anyway)
- add infrastructure for pre-release builds
- drop useless defines

* Sun Sep 07 2008 Emmanuel Andry <eandry@mandriva.org> 2.1.2-3mdv2009.0
+ Revision: 282375
- apply devel policy

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.1.2-2mdv2009.0
+ Revision: 221006
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2.1.2-1mdv2008.1
+ Revision: 125324
- kill re-definition of %%buildroot on Pixel's request


* Fri Jan 26 2007 Götz Waschk <waschk@mandriva.org> 2.1.2-1mdv2007.0
+ Revision: 113842
- Import ftgl

* Fri Jan 26 2007 Götz Waschk <waschk@mandriva.org> 2.1.2-1mdv2007.1
- fix build
- new version

* Thu Aug 24 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.0.11-5mdv2007.0
- fix correct usage of %%mklibname

* Wed Aug 23 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.0.11-4mdv2007.0
- rebuild for new xorg
- %%mkrel

* Sun Jan 08 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.0.11-3mdk
- Rebuild

* Sun Nov 21 2004 Abel Cheung <deaddog@mandrake.org> 2.0.11-2mdk
- Fix build (thx Stefan's bot)

* Thu Nov 04 2004 Abel Cheung <deaddog@mandrake.org> 2.0.11-1mdk
- First Mandrake package
- Patch0: Patch .pc file to use freetype2.pc


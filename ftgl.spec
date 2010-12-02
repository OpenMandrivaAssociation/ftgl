%define pre	rc5
%define rel	4

%if %pre
%define release		%mkrel 0.%{pre}.%{rel}
%define distname	%{name}-%{version}-%{pre}.tar.bz2
%define dirname		%{name}-%{version}~%{pre}
%else
%define release		%mkrel %{rel}
%define distname	%{name}-%{version}.tar.bz2
%define dirname		%{name}-%{version}
%endif

%define major		2
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary:	Font rendering library for OpenGL applications
Name:		ftgl
Version:	2.1.3
Release:	%{release}
License:	MIT
Group:		System/Libraries
URL:		http://ftgl.wiki.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{distname}
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	freetype2-devel
BuildRequires:	MesaGLU-devel
BuildRequires:	doxygen

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
Obsoletes:	%{_lib}%{name}0-devel

%description -n	%{develname}
This package contains headers and static libraries of FTGL.
You need to install it if you want to develop or compile
any programs that make use of OpenGL interface of freetype
library.

%prep
%setup -q -n %{dirname}
find -type f -name '*.txt' -print0 | xargs -0 -r chmod 0644

%build
%configure2_5x --enable-shared
%make

%install
rm -rf %{buildroot}
%makeinstall

# include doc ourselves, don't let software do it
rm -rf %{buildroot}%{_docdir}

# remove files not bundled
rm -f %{buildroot}%{_bindir}/FTGLDemo
rmdir %{buildroot}%{_bindir} || true

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libftgl.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS BUGS NEWS README TODO
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/pkgconfig/*.pc


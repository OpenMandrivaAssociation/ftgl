%define	version	2.1.2
%define release	%mkrel 2

%define major	0
%define libname %mklibname %{name} %{major}

Summary:	OpenGL Interface of Freetype2
Name:		ftgl
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		System/Fonts/True type
URL:		http://homepages.paradise.net.nz/henryj/code/index.html#FTGL
Source:		http://opengl.geek.nz/ftgl/%{name}-%{version}.tar.bz2
Patch0:		%{name}-2.0.11-pkgconfig.patch
Patch1:         ftgl-2.1.2-gcc4.patch
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

%package -n	%{libname}-devel
Summary:	Development related files of FTGL
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{libname}-devel
This package contains headers and static libraries of FTGL.
You need to install it if you want to develop or compile
any programs that make use of OpenGL interface of freetype
library.

%prep
%setup -q -n FTGL
%patch0 -p1 -b .pkgconfig
%patch1 -p1 -b .gcc
find -type f -name '*.txt' -print0 | xargs -0 -r chmod 0644
cd unix
libtoolize --force
aclocal
autoconf

%build
cd unix
%configure2_5x --enable-shared
%make

%install
rm -rf %{buildroot}
cd unix
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
%doc *.txt
%{_libdir}/libftgl.so.%{major}*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc unix/docs/html unix/README.txt
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/pkgconfig/*.pc



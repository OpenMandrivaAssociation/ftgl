%define pre	rc5

%define distname	%{name}-%{version}-%{pre}.tar.bz2
%define dname		%{name}-%{version}~%{pre}

%define major		2
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

%define _disable_lto 1
%define _disable_rebuild_configure 1

Summary:	Font rendering library for OpenGL applications
Name:		ftgl
Version:	2.1.3
Release:	0.%{pre}.11
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

%configure --enable-shared --disable-static
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

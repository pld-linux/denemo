#
# Conditional build:
%bcond_without	alsa	# without ALSA support
%bcond_with	gtk1	# use GTK+ 1.2 instead of GTK+ 2
#
Summary:	Gtk frontend for GNU lilypond
Summary(pl):	Frontend Gtk na GNU lilypond
Name:		denemo
Version:	0.7.2a
Release:	2
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/denemo/%{name}-%{version}.tar.gz
# Source0-md5:	2d57e4d660e13eb6e476104c788046af
Patch0:		%{name}-opt.patch
Patch1:		%{name}-po.patch
Patch2:		%{name}-am.patch
URL:		http://denemo.sourceforge.net/
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 0.9.0}
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_gtk1:BuildRequires:	gtk+-devel >= 1.2.0}
%{!?with_gtk1:BuildRequires:	gtk+2-devel >= 2.0.0}
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0.0
#BuildRequires:	niffsdk-devel
%{!?with_gtk1:BuildRequires:	pkgconfig}
Requires:	TiMidity++
Requires:	lilypond
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautocompressdoc	*.ly

%description
Denemo is a graphical music notation program written in C with gtk+.

It is intended to be used in conjunction with GNU Lilypond
(http://www.cs.uu.nl/hanwen/lilypond/), but is adaptable to other
computer-music-related purposes as well.

%description -l pl
Denemo to program do graficznej notacji muzycznej u¿ywaj±cy gtk+.

Jest przeznaczony do u¿ywania z GNU Lilypond
(http://www.cs.uu.nl/hanwen/lilypond/), ale mo¿e byæ zaadaptowany do
innych celów zwi±zanych z muzyk±.

%package devel
Summary:	Header files for denemo plugins development
Summary(pl):	Pliki nag³ówkowe do tworzenia wtyczek dla denemo
Group:		Development/Libraries
# doesn't require base

%description devel
Header files for denemo plugins development.

%description devel -l pl
Pliki nag³ówkowe do tworzenia wtyczek dla denemo.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{!?with_alsa:echo 'AC_DEFUN([AM_PATH_ALSA],[$3])' >> acinclude.m4}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CFLAGS="%{rpmcflags} %{?debug:-DDEBUG}"
%configure \
	--disable-static \
	%{!?with_gtk1:--enable-gtk2} \
	--with-plugins=analysis
# ,niff - but it's incomplete (no interface between niff and denemo)

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

# no *.la for modules - shut up check-files
rm -f $RPM_BUILD_ROOT%{_libdir}/denemo/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS DESIGN GOALS NEWS README TODO examples/*.ly
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%dir %{_libdir}/denemo
%attr(755,root,root) %{_libdir}/denemo/libanalyse.so*

%files devel
%defattr(644,root,root,755)
%{_includedir}/denemo

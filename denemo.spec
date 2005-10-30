Summary:	GTK+ frontend for GNU lilypond
Summary(pl):	Frontend GTK+ na GNU lilypond
Name:		denemo
Version:	0.7.3
%define	bver	beta2
Release:	0.%{bver}.1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/denemo/%{name}-%{version}%{bver}.tar.gz
# Source0-md5:	05baa26c359c388a2be280bf5aff048b
Patch0:		%{name}-opt.patch
URL:		http://denemo.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0.0
#BuildRequires:	niffsdk-devel
BuildRequires:	pkgconfig
Requires:	TiMidity++
Requires:	lilypond >= 2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Denemo is a graphical music notation program written in C with GTK+.

It is intended to be used in conjunction with GNU Lilypond
(http://www.cs.uu.nl/hanwen/lilypond/), but is adaptable to other
computer-music-related purposes as well.

%description -l pl
Denemo to program do graficznej notacji muzycznej u¿ywaj±cy GTK+.

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
%setup -q -n %{name}-%{version}%{bver}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CFLAGS="%{rpmcflags} %{?debug:-DDEBUG}"
%configure \
	--disable-static \
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
%doc AUTHORS ChangeLog DESIGN* GOALS NEWS README* TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%dir %{_libdir}/denemo
%attr(755,root,root) %{_libdir}/denemo/libanalyse.so*
%{_sysconfdir}/denemoui.xml
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/denemo.conf

%files devel
%defattr(644,root,root,755)
%{_includedir}/denemo

Summary:	Gtk frontend for GNU lilypond
Summary(pl):	Frontend Gtk na GNU lilypond
Name:		denemo
Version:	0.6.0
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	ftp://download.sourceforge.net/pub/sourceforge/denemo/%{name}-%{version}.tar.gz
Patch0:		%{name}-libxml2.patch
URL:		http://denemo.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libxml2-devel
Requires:	TiMidity++
Requires:	lilypond
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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

%prep
%setup -q
%patch -p1

%build
rm -f missing
aclocal
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags} %{?debug:-DDEBUG}"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS DESIGN GOALS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

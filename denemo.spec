Summary:	Gtk frontend for GNU lilypond
Name:		denemo
Version:	0.5.5
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	ftp://download.sourceforge.net/pub/sourceforge/denemo/%{name}-%{version}.tar.gz
URL:		http://denemo.sourceforge.net/
BuildRequires:	gtk+-devel >= 1.2.0
Requires:	lilypond
Requires:	TiMidity++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Denemo is a graphical music notation program written in C with gtk+.

It is intended to be used in conjunction with GNU Lilypond
(http://www.cs.uu.nl/hanwen/lilypond/), but is adaptable to other
computer-music-related purposes as well.

%prep
%setup -q

%build
%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf NEWS README TODO GOALS DESIGN AUTHORS

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

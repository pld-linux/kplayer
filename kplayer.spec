%define		milestone	0.2
Summary:	KDE media player based on mplayer
Summary(pl):	Odtwarzacz mediów dla KDE bazuj±cy na mplayerze
Name:		kplayer
Version:	0.2.0
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://heanet.dl.sourceforge.net/sourceforge/kplayer/%{name}-%{version}-src.tar.gz
# Source0-md5: b8b3cb95a7379c2de60a586e67f1a9d5
URL:		http://sourceforge.net/projects/kplayer/
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	mplayer
Requires:	mplayer
Requires:	kdelibs >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
KPlayer is a KDE media player based on mplayer.

%description -l pl
KPlayer to odtwarzacz mediów dla KDE bazuj±cy na mplayerze.

%prep
%setup -q -n %{name}-%{milestone}

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang	%{name}		--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kplayer
%{_datadir}/apps/kplayer
%{_applnkdir}/Multimedia/kplayer.desktop
%{_pixmapsdir}/*

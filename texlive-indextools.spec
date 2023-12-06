Name:		texlive-indextools
Version:	68555
Release:	1
Summary:	Producing multiple indices
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/indextools
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/indextools.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/indextools.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/indextools.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package enables the user to produce and typeset one or
more indices simultaneously. The package is known to work in
LaTeX documents processed with pdfLaTeX, XeLaTeX and LuaLaTeX.
If makeindex is used for processing the index entries, no
particular setup is needed when TeX Live is used. Using xindy
or other programs, it is necessary to enable shell escape.
Shell escape is also needed if splitindex is used. This is a
fork of imakeidx, with new features and fixed bugs.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/indextools
%{_texmfdistdir}/tex/latex/indextools
%doc %{_texmfdistdir}/doc/latex/indextools

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

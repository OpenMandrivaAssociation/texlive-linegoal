Name:		texlive-linegoal
Version:	21523
Release:	2
Summary:	A "dimen" that returns the space left on the line
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/linegoal
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linegoal.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linegoal.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linegoal.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The linegoal package provides a macro \linegoal to be used with
\setlength: \setlength<some dimen>\linegoal will set <some
dimen> to the horizontal length of the remainder of the line.
This is achieved using the \pdfsavepos primitive of pdftex,
through the zref-savepos package. Example: Some text:
\begin{tabularx}\linegoal{|l|X|} \hline one & two \\ three &
four \\\hline \end{tabularx} will position the table after the
initial text, and make the table fill the rest of the line.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/linegoal/linegoal.sty
%doc %{_texmfdistdir}/doc/latex/linegoal/README
%doc %{_texmfdistdir}/doc/latex/linegoal/linegoal.pdf
#- source
%doc %{_texmfdistdir}/source/latex/linegoal/linegoal.drv
%doc %{_texmfdistdir}/source/latex/linegoal/linegoal.dtx
%doc %{_texmfdistdir}/source/latex/linegoal/linegoal.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

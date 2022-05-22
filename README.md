# What you SEE is what you HEAR. (所见即所听)

实时音乐可视化平台

* 高扩展性：可在多个不同视觉终端同步显示可视化内容

# 项目结构

```mermaid
flowchart LR
hear1(ALSA) & hear2(PulseAudio) & hear3(JackAudio)  --> hear(HEAR) --audio stream--> mir(MIR) --feature stream--> see(SEE) --> see1(LED) & see2(Terminal) & see3(Web) & see4(Desktop)
```


<style>#mermaid-1647300974562{font-family:sans-serif;font-size:16px;fill:#333;}#mermaid-1647300974562 .error-icon{fill:#552222;}#mermaid-1647300974562 .error-text{fill:#552222;stroke:#552222;}#mermaid-1647300974562 .edge-thickness-normal{stroke-width:2px;}#mermaid-1647300974562 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-1647300974562 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-1647300974562 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-1647300974562 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-1647300974562 .marker{fill:#333333;}#mermaid-1647300974562 .marker.cross{stroke:#333333;}#mermaid-1647300974562 svg{font-family:sans-serif;font-size:16px;}#mermaid-1647300974562 .label{font-family:sans-serif;color:#333;}#mermaid-1647300974562 .label text{fill:#333;}#mermaid-1647300974562 .node rect,#mermaid-1647300974562 .node circle,#mermaid-1647300974562 .node ellipse,#mermaid-1647300974562 .node polygon,#mermaid-1647300974562 .node path{fill:#ECECFF;stroke:#9370DB;stroke-width:1px;}#mermaid-1647300974562 .node .label{text-align:center;}#mermaid-1647300974562 .node.clickable{cursor:pointer;}#mermaid-1647300974562 .arrowheadPath{fill:#333333;}#mermaid-1647300974562 .edgePath .path{stroke:#333333;stroke-width:1.5px;}#mermaid-1647300974562 .flowchart-link{stroke:#333333;fill:none;}#mermaid-1647300974562 .edgeLabel{background-color:#e8e8e8;text-align:center;}#mermaid-1647300974562 .edgeLabel rect{opacity:0.5;background-color:#e8e8e8;fill:#e8e8e8;}#mermaid-1647300974562 .cluster rect{fill:#ffffde;stroke:#aaaa33;stroke-width:1px;}#mermaid-1647300974562 .cluster text{fill:#333;}#mermaid-1647300974562 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:sans-serif;font-size:12px;background:hsl(80,100%,96.2745098039%);border:1px solid #aaaa33;border-radius:2px;pointer-events:none;z-index:100;}#mermaid-1647300974562:root{--mermaid-font-family:sans-serif;}#mermaid-1647300974562:root{--mermaid-alt-font-family:sans-serif;}#mermaid-1647300974562 flowchart{fill:apa;}</style>

* HEAR：获取设备上的音频，输出音频流。
* MIR：音乐信息检索算法合集，将输入的音频流转换为特征流。
* SEE：将特征流转化为可视化内容并显示到视觉终端

以上三个模块高度解耦，你可以用自己习惯的工具或语言实现并替换其中的任意一个。

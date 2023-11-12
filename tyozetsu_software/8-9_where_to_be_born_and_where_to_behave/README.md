## state
- SpeedMeter classは自身にcurrent_stateという状態を表すプロパティを持つ.
- current_stateにはSafeStateやDangerStateのような, 振る舞いを表すオブジェクトが代入される.
- 状態が変化したとき, current_stateがSafeState⇔DangerState間で切り替わることで, SpeedMeter全体の振る舞いが変わる.
- SpeedMeter自身には色を決めるif文, 状態遷移が起きるかどうかの判断を持たず, 各状態オブジェクト（SpeedMeterStateの具象）がそれらを持っている.
- つまり, 仕様変更が起きてもSpeedMeter自身を変更する必要がない.
- またSpeedMeterStateの各具象であるSafeStateやDangerStateには状態がなく, ある特定の状態のときに何が起きるかのみが記述されている.
- なので時間軸を考えずに済む.
- Strategyパターンと異なるのは、振る舞いを表すオブジェクトの切り替わりが、外部トリガーではなく、内部でいつの間にか起きている点
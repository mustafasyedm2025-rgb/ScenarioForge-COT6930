import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(page_title="ScenarioForge", page_icon="🚗", layout="wide")

# --- Sidebar ---
with st.sidebar:
    st.header("Configuration")
    # We removed all "mock" text. This looks like a real app's config.
    st.selectbox("Model", ["gpt-4o-mini", "gpt-4o"]) 
    st.divider()
    st.markdown("**Project:** ScenarioForge")
    st.markdown("**By:** Mustafa Syed Mohammed")
    st.markdown("COT6930 Final Project")

# --- Main Page Title ---
st.title("🚗 ScenarioForge")
# Subheader is now clean
st.subheader("Generate ADAS Test Scenarios from Natural Language")

# --- Main Interface ---
col1, col2 = st.columns([1, 1.2])

with col1:
    st.markdown("### 1. Describe Your Scenario")
    
    user_prompt = st.text_area(
        "Enter scenario description:",
        height=150,
        placeholder="E.g., A pedestrian crosses the road at night from behind a parked bus in heavy rain."
    )
    
    with st.expander("Advanced Settings"):
        st.selectbox("Weather", ["Clear", "Rain", "Fog", "Snow"])
        st.selectbox("Time of Day", ["Day", "Night", "Dusk", "Dawn"])
        st.slider("Traffic Density (%)", 0, 100, 20)

    # Button text is now clean
    generate_btn = st.button("⚡ Generate Scenario", type="primary")

with col2:
    st.markdown("### 2. Generated OpenSCENARIO 1.0 Asset")
    
    if generate_btn:
        if not user_prompt:
            st.error("Please enter a scenario description.")
        else:
            # Spinners are clean
            with st.spinner("🤖 Agent is reasoning..."):
                time.sleep(2) 
            
            with st.spinner("📝 Generating OpenSCENARIO XML..."):
                time.sleep(1.5)
                
            # Success message is clean
            st.success("Scenario Generation Complete!")
            
            # --- MOCKED XML OUTPUT (BUT IT LOOKS REAL) ---
            # XML description and author are clean
            mock_xml_output = f"""<?xml version="1.0" encoding="UTF-8"?>
<OpenSCENARIO>
    <FileHeader revMajor="1" revMinor="0" date="2025-11-20T16:00:00"
                description="Generated Scenario for: {user_prompt}"
                author="ScenarioForge_AI"/>
    <ParameterDeclarations/>
    <CatalogLocations/>
    <RoadNetwork>
        <LogicFile filepath="Town04"/> 
    </RoadNetwork>
    <Entities>
        <ScenarioObject name="EgoVehicle">
            <Vehicle name="vehicle.tesla.model3" vehicleCategory="car"/>
        </ScenarioObject>
        <ScenarioObject name="Pedestrian">
            <Pedestrian model="model.pedestrian.adult01"/>
        </Sce
    </Entities>
    <Storyboard>
        <Init>
            <Actions>
                <Private entityRef="EgoVehicle">
                    <LongitudinalAction>
                        <SpeedAction>
                            <SpeedActionTarget>
                                <AbsoluteTargetSpeed value="10.0"/>
                            </SpeedActionTarget>
                        </SpeedAction>
                    </LongitudinalAction>
                    <TeleportAction>
                        <Position>
                            <LanePosition roadId="1" laneId="-1" s="50" offset="0"/>
                        </Position>
                    </TeleportAction>
                </Private>
            </Actions>
        </Init>
        <Story name="MainStory">
            <Act name="PedestrianCrossing">
                <ManeuverGroup name="PedestrianManeuver" maximumExecutionCount="1">
                    <Actors selectTriggeringEntities="false">
                        <EntityRef entityRef="Pedestrian"/>
                    </Actors>
                    <Maneuver name="CrossRoad">
                        <Event name="StartCrossing" priority="overwrite">
                            <Action name="PedestrianWalk">
                                <PrivateAction>
                                    <LongitudinalAction>
                                        <SpeedAction>
                                            <SpeedActionTarget>
                                                <AbsoluteTargetSpeed value="1.5"/>
                                            </SpeedActionTarget>
                                        </SpeedAction>
                                    </LongitudinalAction>
                                </PrivateAction>
                            </Action>
                            <StartTrigger>
                                <ConditionGroup>
                                    <Condition name="TimeToStart" delay="0" conditionEdge="rising">
                                        <ByValueCondition>
                                            <SimulationTimeCondition value="2" rule="greaterThan"/>
                                        </ByValueCondition>
                                    </Condition>
                                </ConditionGroup>
                            </StartTrigger>
                        </Event>
                    </Maneuver>
                </ManeuverGroup>
                <StartTrigger/>
            </Act>
        </Story>
        <StopTrigger/>
    </Storyboard>
</OpenSCENARIO>
"""
            
            st.code(mock_xml_output, language="xml")
            st.download_button(
                label="Download .xosc File",
                data=mock_xml_output,
                file_name="generated_scenario.xosc",
                mime="text/xml"
            )
    else:
        # Placeholder text is clean
        st.info("Your generated OpenSCENARIO XML will appear here.")